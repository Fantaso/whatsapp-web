<!-- logo -->
<a href="https://www.fantaso.de">
<img src="/readme/fantaso.png" align="right" />
</a>

<!-- header -->
<h1 style="text-align: left; margin-top:0px;">
  Simon, a Python Library for WhatsApp Web Automation
</h1>

> Browser automation for WhatsApp Web service with Python & Selenium.


<!-- build -->
<!-- [![Build Status][travis-image]][travis-link] -->


Project consists to allow a user, with whatsapp installed in their phone,
to connect their phone with whatsapp web service https://web.whatsapp.com and 
to automate the functionalities a user normally performs when using whatsapp as a chat app.

Some functionalities:
1. Reading messages
1. Sending messages
2. Detecting new messages' notifications.
3. Replying to a specific (making a reference to the message you are replying to) message


<br><br>

---
## Index:
- #### Objectives
    - Main Goal & User Story
        - A) detecting new messages
        - B) reading new message(s)
        - C) replying a message
        - D) send a message
- #### Installation & Usage
- #### Code Examples
    - Login into whatsapp web, check you are logged in & logout
    - Get all opened chats, go into the chat, read the last 10 messages from your friend and reply to the most recent message
    - More examples
- #### Information
- #### Maintainer

<br><br>

---
## Objectives
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


## Installation & Usage
Install by simple typing `pip install whatsapp-web` and
in your python file you can use it `import simon`


## Code Examples
For the library we are using the Page Pattern recommended by the selenium
python library.

### Login into whatsapp web, check you are logged in & logout
```python
import time

from selenium import webdriver

from simon.accounts.pages import LoginPage
from simon.header.pages import HeaderPage
from simon.pages import BasePage

# Creating the driver (browser)
driver = webdriver.Firefox()
driver.maximize_window()

# 1. Login
#       and uncheck the remember check box
#       (Get your phone ready to read the QR code)
login_page = LoginPage(driver)
login_page.load()
login_page.remember_me = False
time.sleep(7)


# 2. The base page is inherited by all pages
#       and here you can check whether any
#       page is available on the screen of
#       the browser.

# we don't need to load the pages as whatsapp
# web works as one-page web app
base_page = BasePage(driver)
base_page.is_title_matches()
base_page.is_welcome_page_available()
base_page.is_nav_bar_page_available()
base_page.is_search_page_available()
base_page.is_pane_page_available()
# chat is only available after you open one
base_page.is_chat_page_available()


# 3. Logout
header_page = HeaderPage(driver)
header_page.logout()

# Close the browser
driver.quit()
```

### Get all opened chats, go into the chat, read the last 10 messages from your friend and reply to the most recent message
```python
import time

from selenium import webdriver

from simon.accounts.pages import LoginPage
from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage
from simon.header.pages import HeaderPage


# Creating the driver (browser)
driver = webdriver.Firefox()
driver.maximize_window()

# Login
#       and uncheck the remember check box
#       (Get your phone ready to read the QR code)
login_page = LoginPage(driver)
login_page.load()
time.sleep(7)


# 1. Get all opened chats
#       opened chats are the one chats or conversations
#       you already have in your whatsapp.
#       IT WONT work if you are looking for a contact
#       you have never started a conversation.
pane_page = PanePage(driver)

# get all chats
opened_chats = pane_page.opened_chats

# iterating over them
for oc in opened_chats:
    print(oc.name)  # contact name (as appears on your whatsapp)
    print(oc.icon)  # the url of the image
    print(oc.last_message)
    print(oc.last_message_time)  # datetime object
    print(oc.has_notifications())  # are there unread messages?
    print(oc.notifications)  # returns a integer with the qty of new messages, if there are.


# 2. Go into the chat
#       just click on one to open the chat page
#       (where the conversation is happening)
first_chat = opened_chats[0]
first_chat.click()

# 3. Read the last 10 messages from your contact
chat_page = ChatPage(driver)
msgs = chat_page.messages.newest(10, filterby='contact')

for msg in msgs:
    print(msg.contact) # name (all should be the same)
    print(msg.date)
    print(msg.text)
    print(msg.status)


# 4. Reply to the most recent message
msg = msgs[0]  # get the first of the messages query done in previous step
msg = chat_page.messages.newest(filterby='contact')
# Be careful as library can only now reply to text message
# Replying to a msg type (video, image, giff, etc) is not implemented yet. 
msg.reply("This a reply to a specific text msg.")


# Logout
header_page = HeaderPage(driver)
header_page.logout()

# Close the browser
driver.quit()
```

### More examples
For more functionalities that is offered by the library please check
the [tests](https://github.com/Fantaso/whatsapp-web/tree/master/simon/tests). Here a couple:
- [Send a multi line message](https://github.com/Fantaso/whatsapp-web/blob/75889e0517d2fa0913b52131814d416d908976da/simon/tests/chat.py#L341)
- [Send an animated message](https://github.com/Fantaso/whatsapp-web/blob/75889e0517d2fa0913b52131814d416d908976da/simon/tests/chat.py#L353)
- [Get (If there are any) unread messages](https://github.com/Fantaso/whatsapp-web/blob/75889e0517d2fa0913b52131814d416d908976da/simon/tests/chat.py#L85)
- [Get the oldest message](https://github.com/Fantaso/whatsapp-web/blob/75889e0517d2fa0913b52131814d416d908976da/simon/tests/chat.py#L124)
- [Get all messages (order by default: newest)](https://github.com/Fantaso/whatsapp-web/blob/75889e0517d2fa0913b52131814d416d908976da/simon/tests/chat.py#L157)
- [Get most only your recents messages](https://github.com/Fantaso/whatsapp-web/blob/75889e0517d2fa0913b52131814d416d908976da/simon/tests/chat.py#L190)

_**Note:** If you will try to run the test yourself locally, some of them won't
work as some tests are done offline with some html templates that are not available
in the repo_

<!--
## Whatsapp Web UI
- left side (top-bottom)
  - header (profile, status, new chat, menu)
  - search (chats, groups, contacts[new chat], messages)
  - opened_chats (chat, contact icon, contact name, arrow status, truncated msg, time, new msg notification(opt))

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
-->

<br>

## Information:
| Technology Stack |  |  |
| :- | :-: | :- |
| Python                    | ![language][python]                   | Language |
| Selenium                  | ![selenium][selenium]                 | Browser Automation |
| Whatsapp Web              | ![whatsapp][whatsapp]                 | Chat Service |

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
[whatsapp]: readme/whatsapp.png