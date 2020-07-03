from selenium.webdriver.support.ui import WebDriverWait


class CheckBoxException(Exception):
    pass


class RememberMeCheckBox(object):
    def __set__(self, obj, value: bool):
        """Sets the state of the checkbox."""
        if not self._is_boolean(value):
            raise CheckBoxException("You are working with a checkbox: only booleans accepted.")
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        checkbox = driver.find_element_by_name(self.locator)
        self._set_checkbox(checkbox, value)

    def __get__(self, obj, owner):
        """Gets the current state of the checkbox."""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        return driver.find_element_by_name(self.locator).is_selected()

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
