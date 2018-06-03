import znc

class privatemessagetopics(znc.Module):
    description = "This module allows the user to split privmesgs to a nick into topics, simulated by creating fake nicks as the topic."
    module_types = [znc.CModInfo.UserModule, znc.CModInfo.NetworkModule]

    magicHeaderStart = "<"
    magicHeaderEnd = ">*|"
    
    def OnPrivTextMessage(self, message):
        # does the message have the topic header?
        topic, topicText = self._ParseText(message.GetText())
        if topic:
            # yes, route to new user
            # rebuild the full header, topic is split for future purposes possibly
            nick = message.GetNick()
            nickTopic = self.magicHeaderStart + topic + self.magicHeaderEnd + nick.GetNick()
            nick.SetNick(nickTopic)
            message.SetText(topicText)
            message.SetNick(nick)

        return znc.CONTINUE

    def OnUserTextMessage(self, message):
        # is the message going to a nick that's a topic
        nick, topicHeader = self._ParseTopicNick(message.GetTarget())
        if nick:
            # yes, route to non-topic'ed nick
            print(nick, " ", topicHeader)
            message.SetTarget(nick)
            text = message.GetText()
            text = topicHeader + text
            message.SetText(text)

        return znc.CONTINUE

    def _ParseText(self, text):
        if text.startswith(self.magicHeaderStart):
            end = text.find(self.magicHeaderEnd)
            if end >= len(self.magicHeaderStart) + 1:
                topic = text[len(self.magicHeaderStart): end]
                topicText = text[end + len(self.magicHeaderEnd):]
                return topic, topicText

        return None, None
    
    def _ParseTopicNick(self, topicNick):
        if not topicNick.startswith('#'):
            if topicNick.startswith(self.magicHeaderStart):
                end = topicNick.find(self.magicHeaderEnd)
                if end >= len(self.magicHeaderStart) + 1:
                    nickStart = end + len(self.magicHeaderEnd)
                    nick = topicNick[nickStart:]
                    topicHeader = topicNick[:nickStart]
                    return nick, topicHeader

        return None, None
