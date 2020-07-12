from simon.chat.elements import ChatMessages, MessageWriter

from simon.chat.locators import ChatLocators
from simon.pages import BasePage


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
