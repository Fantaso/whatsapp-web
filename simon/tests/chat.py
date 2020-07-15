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
import datetime
import time
import unittest
import uuid as uuid

from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage
from simon.pages import safe_path
from simon.tests.base import LoggedInTestCase, FileBaseTestCase


class ChatPageTests(FileBaseTestCase):
    driver = None
    file_path = "/home/fantaso/github/el_simon/simon/tests/html/rastri_chat_template_full.html"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.chat_page = ChatPage(cls.driver)
        cls.chat_page.load(safe_path(cls.file_path))

    def test_whatsapp_title_matches(self):
        self.assertIn("WhatsApp", self.driver.title)

    # HEADER
    def test_can_check_contact_chat_status_and_contact_info(self):
        # TODO: provide html templates for distinct cases
        self.assertEqual(self.chat_page.contact_name, "Rastri")
        self.assertEqual(self.chat_page.contact_status, "online")
        icon_file = "file:///home/fantaso/github/el_simon/simon/tests/html/rastri_chat_template_full_files/pp.jpeg"
        self.assertEqual(self.chat_page.icon, icon_file)
        self.assertTrue(self.chat_page.is_contact_online())
        self.assertFalse(self.chat_page.is_contact_typing())

    def test_can_get_chat_tools(self):
        # vague test for now as I dont need this functionality implemented
        # but at least making sure the css selectors are correct
        self.assertEqual(self.chat_page.menu.get_attribute("title"), "Menu")
        self.assertEqual(self.chat_page.attach.get_attribute("title"), "Attach")
        self.assertEqual(self.chat_page.search.get_attribute("title"), "Search…")

    # SEARCHER
    # # can search for a message (by: text, time(approx, range), type)
    # msgs = chat_page.messages.search("a msg that contains some keywords")
    # msgs = chat_page.messages.search_type('video')  # audio, voice recording, link, text, status
    # msgs = chat_page.messages.search_date(datetime.datetime)  # a range of 5 up or down the date
    # msgs = chat_page.messages.search_date(datetime.datetime, datetime.datetime)  # ramge
    # msgs = chat_page.messages.search_last_hour()  # day, week, month, year (order by newest)
    # msgs = chat_page.messages.search_by_hour(4)  # day, week, month, year (order by newest)

    # MESSAGES
    def test_can_read_a_message_details_querying_with_newest(self):
        msg = self.chat_page.messages.newest()
        self.assertEqual(msg.contact, "Rastri")
        self.assertEqual(msg.date, datetime.datetime(2020, 7, 8, 20, 33, 00))
        self.assertEqual(msg.text, "Lslsls")
        self.assertIsNone(msg.status)  # this message does not have arrow status

    def test_can_read_unread_messages_and_iterate_over_them(self):
        unread_msgs = self.chat_page.messages.unread()

        self.assertEqual(len(unread_msgs), 4)
        # starts at first unread (oldest msg unread)
        self.assertEqual(unread_msgs[0].text, "Isksk")
        self.assertEqual(unread_msgs[1].text, "Jdjs")
        self.assertEqual(unread_msgs[2].text, "Jsjss")
        self.assertEqual(unread_msgs[3].text, "Lslsls")
        # finishes at last unread (newest msg unread)
        for msg in unread_msgs:
            self.assertEqual(msg.contact, "Rastri")
            self.assertEqual(msg.date, datetime.datetime(2020, 7, 8, 20, 33, 00))
            self.assertIsNone(msg.status)  # these msgs dont have arrow statuses

    def test_can_read_most_recent_message(self):
        msg = self.chat_page.messages.newest()
        self.assertEqual(msg.contact, "Rastri")
        self.assertEqual(msg.date, datetime.datetime(2020, 7, 8, 20, 33, 00))
        self.assertEqual(msg.text, "Lslsls")

    def test_can_read_five_most_recent_messages(self):
        msgs = self.chat_page.messages.newest(5)
        self.assertEqual(len(msgs), 5)

        my_msg = msgs[4]
        self.assertEqual(my_msg.text, "Verga loco.. se me borraron 4 manda 4 más ahí.")
        self.assertEqual(my_msg.date, datetime.datetime(2020, 7, 8, 20, 28, 00))
        self.assertEqual(my_msg.contact, "CmrH")
        self.assertIn(my_msg.status, "Delivered")

        # contact
        contact_msgs = msgs[:4]
        self.assertEqual(len(contact_msgs), 4)
        for msg in contact_msgs:
            self.assertEqual(msg.contact, "Rastri")
            self.assertEqual(msg.date, datetime.datetime(2020, 7, 8, 20, 33, 00))
            self.assertIsNone(msg.status)  # this message does not have arrow status

    def test_can_read_oldest_message(self):
        msg = self.chat_page.messages.oldest()
        self.assertEqual(msg.contact, "Rastri")
        self.assertEqual(msg.date, datetime.datetime(2019, 1, 29, 12, 46, 00))
        self.assertEqual(msg.text, "nena aun en vzla?")
        self.assertIsNone(msg.status)  # this message does not have arrow status

    def test_can_read_five_oldest_messages(self):
        msgs = self.chat_page.messages.oldest(5)
        self.assertEqual(len(msgs), 5)

        contact_msg = msgs[0]
        self.assertEqual(contact_msg.text, "nena aun en vzla?")
        self.assertEqual(contact_msg.date, datetime.datetime(2019, 1, 29, 12, 46, 00))
        self.assertEqual(contact_msg.contact, "Rastri")
        self.assertIsNone(contact_msg.status)

        contact_msg = msgs[1]
        self.assertEqual(contact_msg.text, "Mi amor")
        self.assertEqual(contact_msg.date, datetime.datetime(2019, 1, 29, 18, 55, 00))
        self.assertEqual(contact_msg.contact, "CmrH")
        self.assertEqual(contact_msg.status, "Delivered")

        # contact
        my_msgs = msgs[1:]
        self.assertEqual(len(my_msgs), 4)
        for msg in my_msgs:
            self.assertEqual(msg.contact, "CmrH")
            self.assertEqual(msg.status, "Delivered")
            # the time of these 4 messages are between 18:55 and 18:56
            self.assertGreaterEqual(msg.date, datetime.datetime(2019, 1, 29, 18, 55, 00))
            self.assertLessEqual(msg.date, datetime.datetime(2019, 1, 29, 18, 56, 00))

    def test_can_get_all_messages_at_once(self):
        msgs = self.chat_page.messages.all()
        self.assertEqual(len(msgs), 2030)
        # make sure its being ordered by default (newest)

        newest_msg = msgs[0]
        self.assertEqual(newest_msg.date, datetime.datetime(2020, 7, 8, 20, 33, 00))
        self.assertEqual(newest_msg.text, "Lslsls")
        self.assertEqual(newest_msg.contact, "Rastri")

        oldest_msg = msgs[-1]
        self.assertEqual(oldest_msg.date, datetime.datetime(2019, 1, 29, 12, 46, 00))
        self.assertEqual(oldest_msg.text, "nena aun en vzla?")
        self.assertEqual(oldest_msg.contact, "Rastri")

        # SOME objects which are none do not posses a datetime available
        # comparing_date = datetime.datetime(2019, 1, 1, 00, 00, 00)
        # for msg in msgs:
        #     self.assertGreaterEqual(msg.date, comparing_date)
        #     comparing_date = msg.date

    def test_can_read_most_recent_message_from_contact(self):
        msg = self.chat_page.messages.newest(filterby='contact')
        self.assertEqual(msg.contact, "Rastri")
        self.assertEqual(msg.text, "Lslsls")
        self.assertEqual(msg.date, datetime.datetime(2020, 7, 8, 20, 33, 00))

    def test_can_read_oldest_message_from_contact(self):
        msg = self.chat_page.messages.oldest(filterby='contact')
        self.assertEqual(msg.contact, "Rastri")
        self.assertEqual(msg.text, "nena aun en vzla?")
        self.assertEqual(msg.date, datetime.datetime(2019, 1, 29, 12, 46, 00))

    def test_can_read_most_recent_message_from_myself(self):
        msg = self.chat_page.messages.newest(filterby='myself')
        self.assertEqual(msg.contact, "CmrH")
        self.assertEqual(msg.text, "Verga loco.. se me borraron 4 manda 4 más ahí.")
        self.assertEqual(msg.date, datetime.datetime(2020, 7, 8, 20, 28, 00))

    def test_can_read_oldest_message_from_myself(self):
        msg = self.chat_page.messages.oldest(filterby='myself')
        self.assertEqual(msg.contact, "CmrH")
        self.assertEqual(msg.text, "Mi amor")
        self.assertEqual(msg.date, datetime.datetime(2019, 1, 29, 18, 55, 00))

    def test_can_read_ten_msgs_order_by_most_recent_from_contact(self):
        msgs = self.chat_page.messages.newest(10, filterby='contact')

        self.assertEqual(len(msgs), 10)

        newest = msgs[0]
        fifth = msgs[4]
        tenth = msgs[9]

        self.assertEqual(newest.contact, "Rastri")
        self.assertEqual(newest.text, "Lslsls")
        self.assertEqual(newest.date, datetime.datetime(2020, 7, 8, 20, 33, 00))

        self.assertEqual(fifth.contact, "Rastri")
        self.assertEqual(fifth.text, "Loca")
        self.assertEqual(fifth.date, datetime.datetime(2020, 7, 8, 20, 25, 00))

        self.assertEqual(tenth.contact, "Rastri")
        self.assertEqual(tenth.text, "Ha ok")
        self.assertEqual(tenth.date, datetime.datetime(2020, 7, 7, 18, 11, 00))

    def test_can_read_ten_msgs_order_by_oldest_from_contact(self):
        msgs = self.chat_page.messages.oldest(10, filterby='contact')

        self.assertEqual(len(msgs), 10)

        oldest = msgs[0]
        third = msgs[2]
        fourth = msgs[3]

        self.assertEqual(oldest.contact, "Rastri")
        self.assertEqual(oldest.text, "nena aun en vzla?")
        self.assertEqual(oldest.date, datetime.datetime(2019, 1, 29, 12, 46, 00))

        self.assertEqual(third.contact, "Rastri")
        self.assertEqual(third.text, "como viste la cosa")
        self.assertEqual(third.date, datetime.datetime(2019, 1, 29, 19, 15, 00))

        self.assertEqual(fourth.contact, "Rastri")
        self.assertEqual(fourth.text, "a que loco")
        self.assertEqual(fourth.date, datetime.datetime(2019, 1, 29, 19, 19, 00))

    def test_can_ten_all_msgs_order_by_most_recent_from_myself(self):
        msgs = self.chat_page.messages.newest(10, filterby='myself')

        self.assertEqual(len(msgs), 10)

        newest = msgs[0]
        fourth = msgs[3]
        seventh = msgs[6]

        self.assertEqual(newest.contact, "CmrH")
        self.assertEqual(newest.text, "Verga loco.. se me borraron 4 manda 4 más ahí.")
        self.assertEqual(newest.date, datetime.datetime(2020, 7, 8, 20, 28, 00))

        self.assertEqual(fourth.contact, "CmrH")
        self.assertEqual(fourth.text, "Ya la cosa.")
        self.assertEqual(fourth.date, datetime.datetime(2020, 7, 7, 16, 47, 00))

        self.assertEqual(seventh.contact, "CmrH")
        self.assertEqual(seventh.text, "Jajajaja")
        self.assertEqual(seventh.date, datetime.datetime(2020, 7, 6, 15, 1, 00))

    def test_can_read_all_msgs_order_by_oldest_from_myself(self):
        msgs = self.chat_page.messages.oldest(10, filterby='myself')

        self.assertEqual(len(msgs), 10)

        oldest = msgs[0]
        sixth = msgs[5]
        ninth = msgs[8]

        self.assertEqual(oldest.contact, "CmrH")
        self.assertEqual(oldest.text, "Mi amor")
        self.assertEqual(oldest.date, datetime.datetime(2019, 1, 29, 18, 55, 00))

        self.assertEqual(sixth.contact, "CmrH")
        self.assertEqual(sixth.text, "Jjaa")
        self.assertEqual(sixth.date, datetime.datetime(2019, 1, 29, 19, 18, 00))

        self.assertEqual(ninth.contact, "CmrH")
        self.assertEqual(ninth.text, "Si vaca..")
        self.assertEqual(ninth.date, datetime.datetime(2019, 1, 30, 18, 6, 00))

    def test_can_read_all_msgs_order_by_most_recent_from_contact(self):
        msgs = self.chat_page.messages.all(filterby='contact')
        self.assertEqual(len(msgs), 868)
        msg = msgs[0]
        self.assertEqual(msg.text, "Lslsls")

    def test_can_read_all_msgs_order_by_most_recent_from_myself(self):
        msgs = self.chat_page.messages.all(filterby='myself')
        self.assertEqual(len(msgs), 1162)
        msg = msgs[0]
        self.assertEqual(msg.text, "Verga loco.. se me borraron 4 manda 4 más ahí.")

    def test_can_detect_if_chat_is_completely_new(self):
        # can detect if current chat is fresh (new) chat initiated by contact/client
        self.assertFalse(self.chat_page.is_chat_new())

    def test_can_read_messages_notifications_in_arrow_in_go_to_bottom_button(self):
        # with current html template can not test a negative case (if button is not available)
        self.assertIsNotNone(self.chat_page.arrow_button,
                             "The chat page attribute should return an element (selenium object)")
        self.assertTrue(self.chat_page.is_arrow_button_on_screen(),
                        "Not detecting the arrow button on the chat screen")
        self.assertTrue(self.chat_page.is_notification_in_arrow_button(),
                        "Not detecting the amount of new messages notifications on the arrow bottom on the chat screen")
        self.assertEqual(self.chat_page.arrow_button_notification_qty, 4,
                         "Not detecting the 4 new messages notifications on the arrow bottom on the chat screen")


class InteractiveBaseTestCase(LoggedInTestCase):
    WAIT_TIME = 2
    OPENED_CHAT_CONTACT_NAME = "+58 412-7624636"
    SUCCESSFUL_MSG_STATUS = ["Sent", "Delivered"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        pane_page = PanePage(cls.driver)
        pane_page.get_opened_chat(cls.OPENED_CHAT_CONTACT_NAME).click()
        cls.chat_page = ChatPage(cls.driver)


class InteractiveWriterTests(InteractiveBaseTestCase):

    def test_writer_can_send_a_message_in_the_chat(self):
        writer = self.chat_page.writer
        uid = str(uuid.uuid4())
        writer.send_msg(f"Testing sending a unique msg. {uid}")

        # small time for the message to be "Delivered" or "Sent" instead "Pending"
        time.sleep(self.WAIT_TIME)
        msg = self.chat_page.messages.newest()
        self.assertEqual(msg.text, f"Testing sending a unique msg. {uid}")
        self.assertIn(msg.status, self.SUCCESSFUL_MSG_STATUS)
        self.assertNotEqual(msg.text, "Failed")

    def test_writer_can_send_a_multiline_message_in_the_chat(self):
        multiline_msg = ["Line # 1", "Line # 2"]
        writer = self.chat_page.writer
        writer.send_multiline_msg(multiline_msg)

        # small time for the message to be "Delivered" or "Sent" instead "Pending"
        time.sleep(self.WAIT_TIME)
        msg = self.chat_page.messages.newest()
        self.assertEqual(msg.text, "Line # 1\nLine # 2")
        self.assertIn(msg.status, self.SUCCESSFUL_MSG_STATUS)
        self.assertNotEqual(msg.text, "Failed")

    def test_writer_can_send_a_message_in_the_chat_animated(self):
        writer = self.chat_page.writer
        uid = str(uuid.uuid4())
        writer.send_msg_animated(f"Testing sending a unique animated msg. {uid}",
                                 groove=0.25)

        # small time for the message to be "Delivered" or "Sent" instead "Pending"
        time.sleep(self.WAIT_TIME)
        msg = self.chat_page.messages.newest()
        self.assertEqual(msg.text, f"Testing sending a unique animated msg. {uid}")
        self.assertIn(msg.status, self.SUCCESSFUL_MSG_STATUS)
        self.assertNotEqual(msg.text, "Failed")


class InteractiveTests(InteractiveBaseTestCase):

    def test_can_reply_to_a_specific_message(self):
        """
        Only working to reply any msg that is coming from your contact.
        To reply a msg you send yourself, you need to use diff css selectors and so on.
        """
        # Test that it can reply just to text messages.
        # voice or videos is diffrernt for the css selector

        msg = self.chat_page.messages.newest(filterby='contact')
        uid = str(uuid.uuid4())
        msg.reply(f"Testing a unique reply to a specific msg. {uid} filterby by contact.")

        # small time for the message to be "Delivered" or "Sent" instead "Pending"
        time.sleep(self.WAIT_TIME)
        # TODO: IMPORTANT.. getting the newest() does not ensure the msg to reply will be from your contact
        #       as messages returns all messages found in the chat
        new_msg = self.chat_page.messages.newest()
        self.assertEqual(new_msg.text, f"Testing a unique reply to a specific msg. {uid} filterby by contact.")


if __name__ == "__main__":
    unittest.main()
