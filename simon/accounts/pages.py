from simon.accounts.elements import LoginRememberMeCheckBox

from simon.pages import BasePage


class LoginPage(BasePage):
    remember_me = LoginRememberMeCheckBox()

    def is_instruction_title_matches(self):
        return "To use WhatsApp on your computer" in self.driver.page_source

    def is_remember_me_selected(self):
        return self.remember_me is True
