from simon.header.locators import NavBarLocators


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
