import time
import unittest
from pprint import pprint
from unittest import TestCase

from selenium import webdriver

from simon import pages


class BaseFeatureEins:
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com/")
        self.login_page = pages.LoginPage(self.driver)
        time.sleep(12)

    def tearDown(self):
        # time.sleep(10)
        self.driver.quit()


class FeatureEins(BaseFeatureEins, TestCase):
    """Can detect new message(s), read them, analyse it and reply if needed."""

    def test_can_find_opened_chats_section(self):
        opened_chats = pages.PanePage(self.driver)
        self.assertTrue(opened_chats.is_pane_page_available())
        pprint(opened_chats.get_opened_chats_contacts())

    def test_can_find_first_contact_with_new_message(self):
        opened_chats = pages.PanePage(self.driver)
        self.assertTrue(opened_chats.is_new_message_available())

    def test_can_find_new_message_and_click_to_go_to_contact_chat(self):
        opened_chats = pages.PanePage(self.driver)
        # get all opened chats available
        # get attr (nombre, last msg, double arrow, truncated, new msg)
        # if new_message: click to go tchat

        # get first new msg
        new_msg = opened_chats.get_new_message()
        new_msg.click()

        ## read the mesage

        # check that the chat had opended
        chat_page = pages.ChatPage(self.driver)
        # get text elememnt
        # write to texxt element
        # keys.RETUNR to send message

    def test_can_send_a_msg_to_a_contact(self):
        contact_name = "Rastri"


if __name__ == "__main__":
    unittest.main()
