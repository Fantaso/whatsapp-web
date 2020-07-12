import time
from unittest import TestCase

from selenium import webdriver

from simon import pages


class TearDownClass:
    driver = None

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class LoggedInTestCase(TearDownClass, TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        # Manually login in
        cls.login_page = pages.LoginPage(cls.driver)
        cls.login_page.load()
        time.sleep(7)


class FileBaseTestCase(TearDownClass, TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
