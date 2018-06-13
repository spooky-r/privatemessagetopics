# privatemessagetopics.py

privatemessagetopics.py lets the user split up conversations with a nick into multiple topics, if desired.

I, personally, hold about 3 different topics at once with some people and it gets into a big clusterfuck of "which topic were you responding to?" This solves that problem.

If you have the module installed, anybody can speak to you in topics. If the other user does not have the module, it will just appear as "&lt;topic&gt;*|whatever you just said" when they receive the message.

##### Installing ZNC:
---
- using znc version 1.7.0
  + if upgrading znc, the config should be upgraded automatically on znc startup (but keep a backup anyway)
- follow the guides at: https://wiki.znc.in/Installation
- when compiling, you must enable python: https://wiki.znc.in/Modpython#Compiling

##### Installing this module:
---
- put privatemessagetopics in ($HOME or $APPDATA$ or etc)/.znc/modules/privatemessagetopics.py
- load the module in znc on the web control panel OR
- load it in irc:
  + '/query &ast;status loadmod modpython'
  + '/query &ast;status loadmod privatemessagetopics' (can load either --type=user or --type=network)
- don't forget to saveconfig to keep the module loaded next restart.

##### Talking in topics:
---
- To start a topic '/query &lt;topic&gt;*|nick your message here'
  + replace 'topic' with anything, 'nick' with the actual nick you want the message to go to, and 'your message here' with your message.
