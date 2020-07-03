import time
import unittest
from unittest import TestCase

from selenium import webdriver

from simon import pages


class BaseLoginTests:
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com/")
        self.login_page = pages.LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()


class LoginPageTests(BaseLoginTests, TestCase):
    def test_can_open_whatsapp_web(self):
        self.assertTrue(self.login_page.is_title_matches())
        self.assertTrue(self.login_page.is_instruction_title_matches())

    def test_checkbox_remember_me_is_checked_by_default(self):
        self.assertTrue(self.login_page.is_remember_me_selected())

    def test_can_uncheck_checkbox_remember_me(self):
        self.login_page.remember_me = False
        self.assertFalse(self.login_page.is_remember_me_selected())


class ManualLoginTests(BaseLoginTests, TestCase):
    def test_can_login_successfully(self):
        main_page = pages.BasePage(self.driver)
        # time for you to read QR code and access whatsapp
        time.sleep(10)
        self.assertTrue(main_page.is_title_matches())
        self.assertTrue(main_page.is_welcome_page_available())
        self.assertTrue(main_page.is_nav_bar_page_available())
        self.assertTrue(main_page.is_search_page_available())
        # chat is only available after you click on a person to open the chat
        self.assertFalse(main_page.is_chat_page_available())


if __name__ == "__main__":
    unittest.main()
