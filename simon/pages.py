import os
import pathlib
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from .elements import OpenedChats, ChatMessages, MessageWriter, LoginRememberMeCheckBox
from .locators import NavBarLocators, SearchLocators, WelcomeLocators, PaneLocators, ChatLocators


def element_not_found(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoSuchElementException:
            return False

    return wrapper


def safe_path(abs_path):
    path = os.path.abspath(abs_path)
    url = pathlib.Path(path).as_uri()
    # url = "file:///home/$USER/project_folder/html/test_template.html"
    return url


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        return "WhatsApp" in self.driver.title

    def load(self, url=None):
        if not url:
            self.driver.get("https://web.whatsapp.com/")
        else:
            self.driver.get(url)
        time.sleep(2.5)

    def refresh(self):
        self.driver.refresh()

    @element_not_found
    def is_welcome_page_available(self):
        if self.driver.find_element(*WelcomeLocators.WELCOME):
            return True

    @element_not_found
    def is_nav_bar_page_available(self):
        if self.driver.find_element(*NavBarLocators.BAR):
            return True

    @element_not_found
    def is_search_page_available(self):
        if self.driver.find_element(*SearchLocators.SEARCH):
            return True

    @element_not_found
    def is_pane_page_available(self):
        if self.driver.find_element(*PaneLocators.PANE):
            return True

    @element_not_found
    def is_chat_page_available(self):
        if self.driver.find_element(*ChatLocators.CHAT):
            return True

    def _find_element(self, locator):
        try:
            WebDriverWait(self.driver, 100).until(
                lambda driver: self.driver.find_element(*locator))
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return None


class LoginPage(BasePage):
    remember_me = LoginRememberMeCheckBox()

    def is_instruction_title_matches(self):
        return "To use WhatsApp on your computer" in self.driver.page_source

    def is_remember_me_selected(self):
        return self.remember_me is True


class NavBarPage(BasePage):
    def is_profile_icon_available(self):
        if self.driver.find_element(*NavBarLocators.BAR_PROFILE):
            return True

    def is_status_icon_available(self):
        if self.driver.find_element(*NavBarLocators.BAR_STATUS):
            return True

    def is_new_chat_icon_available(self):
        if self.driver.find_element(*NavBarLocators.BAR_NEW_CHAT):
            return True

    def is_menu_icon_available(self):
        if self.driver.find_element(*NavBarLocators.BAR_MENU):
            return True


class SearchPage(BasePage):
    pass


class PanePage(BasePage):
    opened_chats = OpenedChats()

    def get_first_opened_chat_with_notifications(self):
        for chat in self.opened_chats:
            if chat.has_notifications():
                return chat


class ChatPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.messages = ChatMessages(driver)
        self.writer = MessageWriter(driver)

    def refresh(self):
        self.messages = ChatMessages(self.driver)

    def is_chat_new(self):
        msgs = self.messages.all()
        unread_msgs = self.messages.unread()
        if msgs and unread_msgs:
            if len(msgs) == len(unread_msgs):
                # I could check that the msg is not myself.
                return True

    # Header
    @property
    def contact_name(self):
        return self._find_element(ChatLocators.CHAT_HEADER_CONTACT_NAME).text

    @property
    def contact_status(self):
        return self._find_element(ChatLocators.CHAT_HEADER_CONTACT_STATUS).text

    @property
    def icon(self):
        return self._find_element(ChatLocators.CHAT_HEADER_CONTACT_ICON).get_attribute("src")

    def is_contact_online(self):
        status = self._find_element(ChatLocators.CHAT_HEADER_CONTACT_STATUS).text
        if status and status == "online":
            return True

    def is_contact_typing(self):
        # Not yet tested when the status is Typing...
        statuses = ["yping"]
        status = self._find_element(ChatLocators.CHAT_HEADER_CONTACT_STATUS)
        if status and (status in statuses):
            return True

    @property
    def menu(self):
        return self._find_element(ChatLocators.CHAT_HEADER_MENU)

    @property
    def attach(self):
        return self._find_element(ChatLocators.CHAT_HEADER_ATTACH)

    @property
    def search(self):
        return self._find_element(ChatLocators.CHAT_HEADER_SEARCH)

    # Messages
    @property
    def arrow_button(self):
        return self._find_element(ChatLocators.CHAT_BODY_ARROW_BUTTON)

    @property
    def arrow_button_notification_qty(self):
        if self.is_arrow_button_on_screen():
            qty = self._find_element(ChatLocators.CHAT_BODY_ARROW_BUTTON_NOTIFICATION_QTY).text
            return int(qty)

    def is_arrow_button_on_screen(self):
        if self.arrow_button:
            return True

    def is_notification_in_arrow_button(self):
        if self.arrow_button:
            if self.arrow_button_notification_qty:
                return True


class WelcomePage(BasePage):
    def is_welcome_message_matches(self):
        return "Keep your phone connected" in self.driver.page_source
