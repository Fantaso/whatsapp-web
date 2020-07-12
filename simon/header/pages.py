from simon.header.locators import HeaderLocators
from simon.pages import BasePage


class HeaderPage(BasePage):

    @property
    def profile(self):
        return self._find_element(HeaderLocators.HEADER_PROFILE)

    @property
    def status(self):
        return self._find_element(HeaderLocators.HEADER_STATUS)

    @property
    def new_chat(self):
        return self._find_element(HeaderLocators.HEADER_NEW_CHAT)

    @property
    def menu(self):
        return self._find_element(HeaderLocators.HEADER_MENU)

    @property
    def menu_create_group(self):
        return self._find_element(HeaderLocators.HEADER_MENU_POP_MENU_CREATE_GROUP)

    @property
    def menu_create_room(self):
        return self._find_element(HeaderLocators.HEADER_MENU_POP_MENU_CREATE_ROOM)

    @property
    def menu_profile(self):
        return self._find_element(HeaderLocators.HEADER_MENU_POP_MENU_PROFILE)

    @property
    def menu_archived(self):
        return self._find_element(HeaderLocators.HEADER_MENU_POP_MENU_ARCHIVED)

    @property
    def menu_starred(self):
        return self._find_element(HeaderLocators.HEADER_MENU_POP_MENU_STARRED)

    @property
    def menu_settings(self):
        return self._find_element(HeaderLocators.HEADER_MENU_POP_MENU_SETTINGS)

    @property
    def menu_logout(self):
        return self._find_element(HeaderLocators.HEADER_MENU_POP_MENU_LOGOUT)

    def logout(self):
        self.menu.click()
        self.menu_logout.click()

    def is_profile_icon_available(self):
        if self.profile:
            return True

    def is_status_icon_available(self):
        if self.status:
            return True

    def is_new_chat_icon_available(self):
        if self.new_chat:
            return True

    def is_menu_icon_available(self):
        if self._find_element(HeaderLocators.HEADER_MENU):
            return True
