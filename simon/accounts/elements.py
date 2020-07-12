from selenium.webdriver.support.wait import WebDriverWait

from simon.accounts.locators import LoginLocators


class CheckBoxException(Exception):
    pass


class RememberMeCheckBox(object):
    locator = None

    def __set__(self, instance, value: bool):
        """Sets the state of the checkbox."""
        if not self._is_boolean(value):
            raise CheckBoxException("You are working with a checkbox: only booleans accepted.")
        driver = instance.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        checkbox = driver.find_element(*self.locator)
        self._set_checkbox(checkbox, value)

    def __get__(self, instance, owner):
        """Gets the current state of the checkbox."""
        driver = instance.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        return driver.find_element(*self.locator).is_selected()

    @staticmethod
    def _is_boolean(value):
        if (value is True) or (value is False):
            return True

    @staticmethod
    def _set_checkbox(checkbox, value):
        """
        avoiding to do anything is the wanted stated
        of the checkbox is the current value.
        """
        if value is True and not checkbox.is_selected():
            checkbox.click()
        if value is False and checkbox.is_selected():
            checkbox.click()


class LoginRememberMeCheckBox(RememberMeCheckBox):
    locator = LoginLocators.REMEMBER_ME_CHECKBOX
