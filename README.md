<!-- logo -->
<a href="https://www.fantaso.de">
<img src="/readme/fantaso.png" align="right" />
</a>

<!-- header -->
<h1 style="text-align: left; margin-top:0px;">
  Python Library for WhatsApp Web Automation
</h1>

> Browser automation for WhatsApp Web service with Python & Selenium.


<!-- build -->
<!-- [![Build Status][travis-image]][travis-link] -->


Project consists to allow a user, with a whatsapp installed in their phone,
to automate the functionalities that you can you normally with whatsapp such as:
 1. sending messages to any contact
 2. detecting notifications when new messages arrive.
 3. replying to a specific (making a reference to the message you are replying to) message
 

<br><br>

---
## Index:
- #### Objectives
    - Main Goal & User Story
        - A) detecting new messages
        - B) reading new message(s)
        - C) replying a message
        - D) send a message

- #### Whatsapp Web UI
- #### GOAL

    
- #### Information
- #### Maintainer

<br><br>


---
## Objectives

---
### Main Goal & User Story
Simon can detect new message(s), read them, analyse it and reply if needed.

#### A) detecting new messages
 1. get simon_opened_chats
 2. inspect available user from top-bottom for notifications (only on available browser screen view)
 3. click on the opened chat found with a new message notification icon

#### B) reading new message(s)
 1. get contact_chat
 2. find "n unread messages" section
 3. get first unread msg
 4. read and analyse msg

#### C) replying a message
 1. get(hover) the reply icon (on the right-side of the message)
 2. click on the reply icon
 3. get the reply link("Reply")
 4. click the reply link (on browser: it puts cursor on the contact_send_message[message_field])

#### D) send a message
 1. get contact_send_message
 2. write message
 3. press enter to send msg.


---
## Whatsapp Web UI
- left side (top-bottom)
  - simon_detail (profile, status, new chat, menu)
  - simon_search (chats, groups, contacts[new chat], messages)
  - simon_opened_chats (chat, contact icon, contact name, arrow status, truncated msg, time, new msg notification(opt))

    NOTE: chats are visible only when scrolling and are visible on the screen of the browser.
    
- right side (top-bottom)
  - contact_detail (contact icon, contact name, ... , search, attachment, menu)
  - contact_chat (messages)
  - contact_send_message (smileys, message_field, record audio)


------------------------------------------------
------------------------------------------------
#### In Current Chat
- Simon can send a message
- Simon can receive a message
#### ~In Current Chat
- Simon can search people in open chats...

<br>

## Information:
| Technology Stack |  |  |
| :- | :-: | :- |
| Python                    | ![language][python]                   | Language |
| Selenium                  | ![selenium][selenium]                 | Browser Automation |

<br><br>


## Maintainer
Get in touch -–> [fantaso][fantaso]


<!-- Links -->
<!-- Profiles -->
[github-profile]: https://github.com/fantaso/
[linkedin-profile]: https://www.linkedin.com/
[fantaso]: https://github.com/fantaso/
<!-- Extra -->

<!-- Repos -->
[github-repo]: https://github.com/Fantaso/whatsapp-web

<!-- Builds -->
[travis-link]: https://travis-ci.org/
[travis-image]: https://travis-ci.org/

<!-- images -->
[python]: readme/python.png
[selenium]: readme/selenium.png