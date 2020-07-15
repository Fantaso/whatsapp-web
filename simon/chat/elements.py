import datetime
import time
from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from simon.chat.locators import ChatLocators


class Message:
    def __init__(self, element=None, driver=None):
        self.element = element
        self.driver = driver

    def find_element(self, locator):
        """
        Using this for all attrs ensures we are bound to the
        context of the message only(html code of the message only)
        avoiding grabbing other element in the whole html page.
        """
        try:
            # TODO: test the idea of using the self.driver this deep
            #       to refresh DOM elements in the self.element
            if self.element:
                return self.element.find_element(*locator)
        except NoSuchElementException:
            return None

    @property
    def contact(self):
        return self.__get_cleaned_contact()

    @property
    def date(self):
        return self.__get_cleaned_datetime()

    @property
    def text(self):
        if self.find_element(ChatLocators.CHAT_BODY_MSG_TEXT):
            return self.find_element(ChatLocators.CHAT_BODY_MSG_TEXT).text

    @property
    def status(self):
        if self.find_element(ChatLocators.CHAT_BODY_MSG_STATUS):
            return self.find_element(ChatLocators.CHAT_BODY_MSG_STATUS).get_attribute("aria-label").strip()

    def __get_cleaned_contact(self):
        _str = self.raw_datetime_and_contact()
        if _str:
            contact_str = _str.strip().rsplit(" ", 1)[1]
            return contact_str.replace(":", "")

    def __get_cleaned_datetime(self):
        _str = self.raw_datetime_and_contact()
        if _str:
            datetime_str = _str.strip().rsplit(" ", 1)[0]
            return datetime.datetime.strptime(datetime_str, "[%H:%M, %m/%d/%Y]")

    def raw_datetime_and_contact(self):
        if self.find_element(ChatLocators.CHAT_BODY_MSG_CONTACT_AND_DATETIME):
            # "[19:18, 1/29/2019] CmrH: "
            return self.find_element(
                ChatLocators.CHAT_BODY_MSG_CONTACT_AND_DATETIME
            ).get_attribute("data-pre-plain-text")

    def reply(self, msg: str):
        """Only works to reply msgs from the contact.
        DO NOT USE IT to reply your own msg. (Different css selectors needed)"""
        if msg:
            # Hover near by the reply arrow menu
            msg_text = self.find_element(ChatLocators.CHAT_BODY_MSG_TEXT)
            hover = ActionChains(self.driver).move_to_element(msg_text)
            hover.perform()

            # -> BOUND OUT OF html element context and the whole html page
            #    MAYBE in the base page context.
            # get arrow and click on it
            msg_arrow_menu = self.driver.find_element(*ChatLocators.CHAT_BODY_MSG_ARROW)
            msg_arrow_menu.click()

            reply_button = self.driver.find_element(*ChatLocators.CHAT_BODY_MSG_ARROW_POP_MENU_REPLY)
            reply_button.click()

            writer = MessageWriter(self.driver)
            writer.send_msg(msg)
            # <- END OUT OF BOUND
            return "Coders on break!"

    def __repr__(self):
        return f"Message({self.element})"

    def __str__(self):
        return f"{self.contact}: '({self.text})'"


class OnlyFilterByContact(Exception):
    pass


class ChatMessages:
    child_class = Message

    def __init__(self, driver):
        self.driver = driver

    def all(self, filterby: str = None):
        locator = self.get_correct_locator(filterby)
        order_by_oldest = [self.child_class(e, self.driver) for e in self.__find_elements(locator)]
        order_by_newest = order_by_oldest[::-1]
        return order_by_newest

    def get_correct_locator(self, filterby):
        if not filterby:
            return ChatLocators.CHAT_BODY_MSGS
        if filterby == 'contact':
            return ChatLocators.CHAT_BODY_MSGS_CONTACT
        if filterby == 'myself':
            return ChatLocators.CHAT_BODY_MSGS_MYSELF
        else:
            raise OnlyFilterByContact("For now we just can filter by contact name")

    def newest(self, qty: int = None, filterby=None):
        msgs = self.all(filterby)
        return self.__get_correct_qty(qty, msgs)

    def oldest(self, qty: int = None, filterby=None):
        msgs = self.all(filterby)[::-1]
        return self.__get_correct_qty(qty, msgs)

    def unread(self):
        qty = self.unread_qty()
        if qty:
            unread_msgs_by_newest = self.all(filterby='contact')[:qty]
            unread_msgs_by_oldest = unread_msgs_by_newest[::-1]
            return unread_msgs_by_oldest
        return []

    def unread_qty(self):
        if self.__find_element(ChatLocators.CHAT_BODY_UNREAD_MESSAGE):
            text = self.__find_element(ChatLocators.CHAT_BODY_UNREAD_MESSAGE).text
            # "4182 UNREAD MESSAGES"
            qty = text.split(" ", 1)[0]
            return int(qty)

    def __find_elements(self, locator):
        # TODO: THIS DEEP i do not have to worry about the real time
        #       state of the messages. It should hangle upper level.
        #       OR YES I DO? ANALYSE WHEN SEEN!
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_elements(*locator))
        elements = self.driver.find_elements(*locator)
        return [e for e in elements]

    def __find_element(self, locator):
        try:
            WebDriverWait(self.driver, 100).until(
                lambda driver: self.driver.find_element(*locator))
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return None

    def __get_correct_qty(self, qty, msgs):
        if not qty:
            return msgs[0]
        if self._have_enough(qty, len(msgs)):
            return msgs[:qty]
        else:
            return msgs

    @staticmethod
    def _have_enough(qty_asked: int, qty_msgs: int):
        if qty_asked <= qty_msgs:
            return True


class MessageWriter(object):
    def __init__(self, driver):
        self.driver = driver

    def send_msg(self, msg: str):
        text_input = self.__find_element(ChatLocators.CHAT_FOOTER_TEXT_INPUT_FIELD)
        if text_input and msg:
            text_input.send_keys(msg)
            time.sleep(1)
            text_input.send_keys(Keys.RETURN)

    def send_multiline_msg(self, msgs: List[str]):
        text_input = self.__find_element(ChatLocators.CHAT_FOOTER_TEXT_INPUT_FIELD)
        if text_input and msgs:
            time.sleep(1)
            for msg in msgs:
                text_input.send_keys(msg)
                # press SHIFT + ENTER (for new line)
                ActionChains(self.driver).key_down(Keys.SHIFT).send_keys(Keys.RETURN).key_up(Keys.SHIFT).perform()
            text_input.send_keys(Keys.RETURN)

    def send_msg_animated(self, msg, groove=0.22):
        text_input = self.__find_element(ChatLocators.CHAT_FOOTER_TEXT_INPUT_FIELD)
        for char in msg:
            text_input.send_keys(char)
            time.sleep(groove)
        text_input.send_keys(Keys.RETURN)

    def __find_element(self, locator):
        try:
            WebDriverWait(self.driver, 100).until(
                lambda driver: self.driver.find_element(*locator))
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return None
