---
# Simon: the chatbot

---
# Whatsapp Web UI
- left side (top-bottom)
  - simon_detail (profile, status, new chat, menu)
  - simon_search (chats, groups, contacts[new chat], messages)
  - simon_opened_chats (chat, contact icon, contact name, arrow status, truncated msg, time, new msg notification(opt))

    NOTE: chats are visible only when scrolling and are visible on the screen of the browser.
    
- right side (top-bottom)
  - contact_detail (contact icon, contact name, ... , search, attachment, menu)
  - contact_chat (messages)
  - contact_send_message (smileys, message_field, record audio)


---
# GOAL
(1) - Simon can detect new message(s), read them, analyse it and reply if needed.
(2) - Simon can detect when new message is from a fresh(newly) contact, send a welcome message with a menu with FAQ.


---
# USER STORIES
(1) - Simon can detect new message(s), read them, analyse it and reply if needed.

### (a) detecting new msgs
- get simon_opened_chats
- inspect available user from top-bottom for notifications (only on available browser screen view)
- click on the opened chat found with a new message notification icon

### (b) reading new message(s)
- get contact_chat
- find "n unread messages" section
- get first unread msg
- read and analyse msg

### (c) replying a msg
- get(hover) the reply icon (on the right-side of the msg)
- click on the reply icon
- get the reply link("Reply")
- click the reply link (on browser: it puts cursor on the contact_send_message[message_field])

### (d) send a msg
- get contact_send_message
- write message
- press enter to send msg.



---
#### In Current Chat
- Simon can send a message
- Simon can receive a message
#### ~In Current Chat
- Simon can search people in open chats