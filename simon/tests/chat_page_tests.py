## 1st
# can read a message's text, time, arrow, type
# can reply to a (specific) message
## 2nd
# can read most recent message
# can read 5 most recent messages
# can read oldest message available
# can read 5 oldest messages available
# can iterate over all messages (default=most recent)
## 3rd
# can read last unread messages
# can iterate over last unread messages
## 4th
# can detect if current chat is fresh (new) chat initiated by contact/client
## 5th
# can write and send a message
# can send a multiline message
## 6th
# can search for a message (by: text, time(approx, range), type)
## optional
# can send a link
# can send an image
# can send a video
# can send an audio
# can record a voice from microphone
#######################################################
import unittest

from simon.tests.base import LoggedInTestCase


class ChatPageTests(LoggedInTestCase):
    pass


if __name__ == "__main__":
    unittest.main()
