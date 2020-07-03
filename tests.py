import time
import unittest
from pprint import pprint
from unittest import TestCase

from selenium import webdriver

from simon import page


class LoginPageTests(TestCase):
    """Testing Whatsapp web connect your phone page."""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com/")
        self.login_page = page.LoginPage(self.driver)

    def test_can_open_whatsapp_web(self):
        self.assertTrue(self.login_page.is_title_matches())
        self.assertTrue(self.login_page.is_instruction_title_matches())

    def test_checkbox_remember_me_is_checked_by_default(self):
        self.assertTrue(self.login_page.is_remember_me_selected())

    def test_can_uncheck_checkbox_remember_me(self):
        self.login_page.remember_me = False
        self.assertFalse(self.login_page.is_remember_me_selected())

    def tearDown(self):
        self.driver.quit()


class ManuallyLogingInTests(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com/")
        self.login_page = page.LoginPage(self.driver)

    def test_can_login_successfully(self):
        main_page = page.MainPage(self.driver)
        time.sleep(10)
        self.assertTrue(main_page.is_profile_icon_available())
        self.assertTrue(main_page.is_status_icon_available())
        self.assertTrue(main_page.is_new_chat_icon_available())
        self.assertTrue(main_page.is_menu_icon_available())

        self.assertTrue(main_page.is_welcome_message_matches())

    def tearDown(self):
        self.driver.quit()


class FeatureEins(TestCase):
    """Can detect new message(s), read them, analyse it and reply if needed."""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com/")
        self.login_page = page.LoginPage(self.driver)
        time.sleep(12)

    def test_can_find_opened_chats_section(self):
        opened_chats = page.MainPage(self.driver)
        self.assertTrue(opened_chats.is_pane_section_available())
        pprint(opened_chats.get_opened_chats_contacts())

    def test_can_find_first_contact_with_new_message(self):
        opened_chats = page.MainPage(self.driver)
        self.assertTrue(opened_chats.is_new_message_available())

    def test_can_find_new_message_and_click_to_go_to_contact_chat(self):
        opened_chats = page.MainPage(self.driver)
        # get all opened chats available
            # get attr (nombre, last msg, double arrow, truncated, new msg)
            # if new_message: click to go tchat

        # get first new msg
        new_msg = opened_chats.get_new_message()
        new_msg.click()

        ## read the mesage

        # check that the chat had opended
        chat_page = page.ChatPage(self.driver)
        # get text elememnt
        # write to texxt element
        # keys.RETUNR to send message

    def test_can_send_a_msg_to_a_contact(self):
        contact_name = "Rastri"

    # def test_

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
