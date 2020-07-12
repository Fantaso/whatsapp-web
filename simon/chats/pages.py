from simon.chats.elements import OpenedChats

from simon.pages import BasePage


class PanePage(BasePage):
    opened_chats = OpenedChats()

    def get_first_opened_chat_with_notifications(self):
        for chat in self.opened_chats:
            if chat.has_notifications():
                return chat

    def get_opened_chat(self, name):
        for opened_chat in self.opened_chats:
            if name == opened_chat.name:
                return opened_chat
