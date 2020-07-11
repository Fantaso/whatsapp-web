import time
from unittest import TestCase

from selenium import webdriver

from simon import pages


class LoggedInTestCase(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        # Manually login in
        cls.login_page = pages.LoginPage(cls.driver)
        cls.login_page.load()
        time.sleep(7)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
