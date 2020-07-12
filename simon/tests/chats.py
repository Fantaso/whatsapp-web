import unittest

from selenium.webdriver.common.keys import Keys

from simon.chat.locators import ChatLocators  # TODO: this ref should not be coupled with another page
from simon.chats.pages import PanePage
from simon.tests.base import LoggedInTestCase


class PanePageTests(LoggedInTestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.pane_page = PanePage(cls.driver)
        cls.pane_page.load()

    def test_can_get_opened_chats(self):
        self.assertGreaterEqual(len(self.pane_page.opened_chats), 5)

    def test_can_click_in_the_first_opened_chat(self):
        first_chat = self.pane_page.opened_chats[0]
        first_chat.click()
        self.assertIsNotNone(self.driver.find_element(*ChatLocators.CHAT))

    def test_can_get_first_opened_chat_details(self):
        first_chat = self.pane_page.opened_chats[0]
        self.assertIsNotNone(first_chat.name)
        self.assertIsNotNone(first_chat.icon)
        self.assertIsNotNone(first_chat.last_message)
        self.assertIsNotNone(first_chat.last_message_time)

    def test_can_iterate_over_first_five_opened_chats(self):
        for opened_chat in self.pane_page.opened_chats[:5]:
            self.assertIsNotNone(opened_chat.name)
            self.assertIsNotNone(opened_chat.icon)
            self.assertIsNotNone(opened_chat.last_message)
            self.assertIsNotNone(opened_chat.last_message_time)

    def test_can_detect_first_opened_chat_with_new_messages(self):
        chat = self.pane_page.get_first_opened_chat_with_notifications()
        self.assertIsInstance(chat.notifications, int)
        self.assertGreaterEqual(chat.notifications, 1)

    def test_can_detect_first_opened_chat_with_new_messages_and_click_it(self):
        chat = self.pane_page.get_first_opened_chat_with_notifications()
        self.assertGreaterEqual(chat.notifications, 1)
        chat.click()
        self.assertIsNotNone(self.driver.find_element(*ChatLocators.CHAT))
        self.assertIn("unread message", self.driver.page_source.lower())

    def test_can_detect_first_opened_chat_with_new_messages_and_send_a_message(self):
        """
        This a manual test. It will be removed when
        the elements are created for the ChatPage.
        """
        chat = self.pane_page.get_first_opened_chat_with_notifications()
        chat.click()
        chat_text_field = self.driver.find_element(*ChatLocators.CHAT_FOOTER_TEXT_INPUT_FIELD)
        chat_text_field.send_keys("Hi, I am Simon: Carlos's WhatsApp ChatBot!")
        chat_text_field.send_keys(Keys.RETURN)


if __name__ == "__main__":
    unittest.main()
