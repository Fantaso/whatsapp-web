from selenium.common.exceptions import NoSuchElementException

from .elements import LoginRememberMeCheckBox
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

    # main pages
    # def is_login_page_available(self):
    #     if self.driver.find_element():
    #         return True

    def is_welcome_page_available(self):
        if self.driver.find_element(*WelcomeLocators.WELCOME):
            return True

    def is_nav_bar_page_available(self):
        if self.driver.find_element(*NavBarLocators.BAR):
            return True

    def is_search_page_available(self):
        if self.driver.find_element(*SearchLocators.SEARCH):
            return True

    def is_pane_page_available(self):
        if self.driver.find_element(*PaneLocators.PANE):
            return True

    @element_not_found
    def is_chat_page_available(self):
        if self.driver.find_element(*ChatLocators.CHAT):
            return True


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
    def is_new_message_available(self):
        new_msgs = self.driver.find_elements(*PaneLocators.NEW_MESSAGE_ICONS)
        if new_msgs and len(new_msgs) > 0:
            return True

    def get_new_message(self):
        return self.driver.find_element(*PaneLocators.NEW_MESSAGE_ICONS)

    def get_new_messages(self):
        return self.driver.find_elements(*PaneLocators.NEW_MESSAGE_ICONS)

    def get_opened_chats_contacts(self):
        return [contact.text for contact in
                self.driver.find_elements(*PaneLocators.CONTACT_NAMES)]


class ChatPage(BasePage):
    pass


class WelcomePage(BasePage):
    def is_welcome_message_matches(self):
        return "Keep your phone connected" in self.driver.page_source
