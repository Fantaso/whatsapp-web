import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait

from .locators import PaneLocators


class ReadOnlyBaseElement(object):
    def __init__(self, element):
        self.element = element

    def __get__(self, instance, owner):
        return self.element

    def __set__(self, instance, value):
        raise Exception("Can not set a value to a read-only element")

    def __repr__(self):
        return f"<ReadOnlyBaseElement: {self.element}>"


class ReadOnlyBaseElements(object):
    locator = None
    child_class = None

    def __get__(self, instance, owner):
        """Gets the current state of the element."""
        driver = instance.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_elements(*self.locator))
        elements = driver.find_elements(*self.locator)
        return [self.child_class(ele) for ele in elements]

    def __set__(self, instance, values):
        raise Exception("Can not set a value to a read-only elements")


def element_not_found(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoSuchElementException:
            return ""
        except StaleElementReferenceException:
            return ""

    return wrapper


class Chat(ReadOnlyBaseElement):
    @property
    @element_not_found
    def name(self):
        return self.element.find_element(*PaneLocators.NAME).text

    @property
    @element_not_found
    def last_message_time(self):
        return self.element.find_element(*PaneLocators.LAST_MESSAGE_TIME).text

    @property
    @element_not_found
    def last_message(self):
        return self.element.find_element(*PaneLocators.LAST_MESSAGE).text

    @property
    @element_not_found
    def icon(self):
        return self.element.find_element(*PaneLocators.ICON).get_attribute('src')

    @property
    @element_not_found
    def notifications(self):
        return int(self.element.find_element(*PaneLocators.NOTIFICATION).text)

    @element_not_found
    def has_notifications(self):
        notifications = int(self.element.find_element(*PaneLocators.NOTIFICATION).text)
        if notifications > 0:
            return True

    @element_not_found
    def click(self):
        self.element.click()
        time.sleep(3)


class OpenedChats(ReadOnlyBaseElements):
    locator = PaneLocators.OPENED_CHATS
    child_class = Chat


class CheckBoxException(Exception):
    pass


class RememberMeCheckBox(object):
    locator = None

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
