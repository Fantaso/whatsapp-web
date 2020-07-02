from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass


# Page - Left side
class SimonDetailLocators:
    PROFILE = (,)
    STATUS = (,)
    NEW_CHAT = (,)
    MENU = (,)


class SimonSearchLocators:
    SEARCH = (,)
    CHATS = (,)
    GROUPS = (,)
    CONTACTS = (,)  # creating a new chat
    MESSAGES = (,)


class SimonOpenChatsLocators:
    CHATS = (,)
    CHAT = (,)
    CONTACT_ICON = (,)
    CONTACT_NAME = (,)
    ARROW_STATUS = (,)
    TRUNCATED_MSG = (,)
    LAST_MSG_TIME = (,)
    NEW_MESSAGE_ICON = (,)


# Page - Right side
class ContactDetailLocators:
    pass


class ContactChatLocators:
    pass


class ContactSendMessageLocators:
    pass
