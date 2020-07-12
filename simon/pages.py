import os
import pathlib
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from .chat.locators import ChatLocators
from .chats.locators import PaneLocators
from .header.locators import HeaderLocators
from .locators import WelcomeLocators
from .search.locators import SearchLocators


def element_not_found(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoSuchElementException:
            return False

    return wrapper


def safe_path(abs_path):
    path = os.path.abspath(abs_path)
    url = pathlib.Path(path).as_uri()
    # url = "file:///home/$USER/project_folder/html/test_template.html"
    return url


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        return "WhatsApp" in self.driver.title

    def load(self, url=None):
        if not url:
            self.driver.get("https://web.whatsapp.com/")
        else:
            self.driver.get(url)
        time.sleep(2.5)

    def refresh(self):
        self.driver.refresh()

    @element_not_found
    def is_welcome_page_available(self):
        if self._find_element(WelcomeLocators.WELCOME):
            return True

    @element_not_found
    def is_nav_bar_page_available(self):
        if self._find_element(HeaderLocators.HEADER):
            return True

    @element_not_found
    def is_search_page_available(self):
        if self._find_element(SearchLocators.SEARCH):
            return True

    @element_not_found
    def is_pane_page_available(self):
        if self._find_element(PaneLocators.PANE):
            return True

    @element_not_found
    def is_chat_page_available(self):
        if self._find_element(ChatLocators.CHAT):
            return True

    def _find_element(self, locator):
        try:
            WebDriverWait(self.driver, 100).until(
                lambda driver: self.driver.find_element(*locator))
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return None


class WelcomePage(BasePage):
    def is_welcome_message_matches(self):
        return "Keep your phone connected" in self.driver.page_source
