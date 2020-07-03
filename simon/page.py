from .element import RememberMeCheckBox
from .locators import ProfileLocators


class LoginPageRememberMeCheckBox(RememberMeCheckBox):
    locator = "rememberMe"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    remember_me = LoginPageRememberMeCheckBox()

    def is_title_matches(self):
        return "WhatsApp" in self.driver.title

    def is_instruction_title_matches(self):
        return "To use WhatsApp on your computer" in self.driver.page_source

    def is_remember_me_selected(self):
        return self.remember_me is True

class ChatPage(BasePage):
    def is_chat_page_visible(self):
        if self.driver.find_element(*ChatPageLocators.)

class MainPage(BasePage):
    # Profile Section - Simon Detail
    def is_welcome_message_matches(self):
        return "Keep your phone connected" in self.driver.page_source

    def is_profile_icon_available(self):
        if self.driver.find_element(*ProfileLocators.PROFILE):
            return True

    def is_status_icon_available(self):
        if self.driver.find_element(*ProfileLocators.STATUS):
            return True

    def is_new_chat_icon_available(self):
        if self.driver.find_element(*ProfileLocators.NEW_CHAT):
            return True

    def is_menu_icon_available(self):
        if self.driver.find_element(*ProfileLocators.MENU):
            return True

    # Pane Section - Opened Chats
    def is_pane_section_available(self):
        if self.driver.find_element(*ProfileLocators.PANE_SECTION):
            return True

    def is_new_message_available(self):
        new_msgs = self.driver.find_elements(*ProfileLocators.NEW_MESSAGE_ICONS)
        if new_msgs and len(new_msgs) > 0:
            return True

    def get_new_message(self):
        return self.driver.find_element(*ProfileLocators.NEW_MESSAGE_ICONS)

    def get_new_messages(self):
        return self.driver.find_elements(*ProfileLocators.NEW_MESSAGE_ICONS)

    def get_opened_chats_contacts(self):
        return [contact.text for contact in
                self.driver.find_elements(*ProfileLocators.CONTACT_NAMES)]
