import time

from selenium.common.exceptions import NoSuchElementException

from .elements import RememberMeCheckBox, OpenedChats
from .locators import NavBarLocators, SearchLocators, WelcomeLocators, PaneLocators, ChatLocators


def element_not_found(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoSuchElementException:
            return False

    return wrapper


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        return "WhatsApp" in self.driver.title

    def load(self):
        self.driver.get("https://web.whatsapp.com/")
        time.sleep(2.5)

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


class LoginRememberMeCheckBox(RememberMeCheckBox):
    locator = "rememberMe"


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
    pass


class WelcomePage(BasePage):
    def is_welcome_message_matches(self):
        return "Keep your phone connected" in self.driver.page_source
