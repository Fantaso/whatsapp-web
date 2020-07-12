from selenium.webdriver.common.by import By


class LoginLocators(object):
    REMEMBER_ME_CHECKBOX = (By.NAME, "rememberMe")


class NavBarLocators(object):
    # parent
    BAR = (By.CSS_SELECTOR, "._1QUKR")
    # childs
    BAR_PROFILE = (By.CSS_SELECTOR, "._1MXsz ._3Whw5")
    BAR_STATUS = (By.CSS_SELECTOR, ".PVMjB:nth-child(1)")
    BAR_NEW_CHAT = (By.CSS_SELECTOR, ".PVMjB:nth-child(2)")
    BAR_MENU = (By.CSS_SELECTOR, ".PVMjB:nth-child(3)")


class SearchLocators(object):
    SEARCH = (By.CSS_SELECTOR, "._2EoyP")
    # CHATS = (,)
    # GROUPS = (,)
    # CONTACTS = (,)  # creating a new chat
    # MESSAGES = (,)


class PaneLocators(object):
    # parent
    PANE = (By.CSS_SELECTOR, "#pane-side")

    # childs
    OPENED_CHATS = (By.CSS_SELECTOR, "#pane-side ._210SC")

    # grand child of each child
    ## left side
    ICON = (By.CSS_SELECTOR, "._325lp img")  # attr(src)
    ## right side
    ### upper side
    NAME = (By.CSS_SELECTOR, "._2kHpK ._3ko75._5h6Y_")
    LAST_MESSAGE_TIME = (By.CSS_SELECTOR, "._2kHpK .m61XR")
    ### bottom side
    # ARROW_STATUS = (By.CSS_SELECTOR, "._210SC ._1582E .zFnXi")
    LAST_MESSAGE = (By.CSS_SELECTOR, "._2kHpK ._1582E ._3Whw5")
    NOTIFICATION = (By.CSS_SELECTOR, "._210SC .m61XR ._31gEB")


class ChatLocators(object):
    CHAT = (By.CSS_SELECTOR, "#main")

    # CHAT INFO & DETAILS, CHAT MENU & SETTINGS
    CHAT_HEADER = (By.CSS_SELECTOR, "#main header")
    CHAT_HEADER_CONTACT_ICON = (By.CSS_SELECTOR, "#main header ._2goTk")  # attr:(src)
    CHAT_HEADER_CONTACT_NAME = (By.CSS_SELECTOR, "#main header ._3ko75")
    CHAT_HEADER_CONTACT_STATUS = (By.CSS_SELECTOR, "#main header ._3-cMa")
    CHAT_HEADER_MENU = (By.CSS_SELECTOR, "#main header .PVMjB:nth-child(3) div")
    CHAT_HEADER_ATTACH = (By.CSS_SELECTOR, "#main header .PVMjB:nth-child(2) div")
    CHAT_HEADER_SEARCH = (By.CSS_SELECTOR, "#main header .PVMjB:nth-child(1) div")

    # READING MSGS
    CHAT_BODY = (By.CSS_SELECTOR, "#main ._2-aNW .z_tTQ")
    CHAT_BODY_MSGS = (By.CSS_SELECTOR, "._2hqOq.message-in, ._2hqOq.message-out")
    CHAT_BODY_MSG_CONTACT_AND_DATETIME = (By.CSS_SELECTOR, "._3sKvP.wQZ0F ._274yw div.copyable-text")
    CHAT_BODY_MSG_STATUS = (By.CSS_SELECTOR, "._3sKvP.wQZ0F ._274yw div._2frDn ._1qPwk span")
    CHAT_BODY_MSG_TEXT = (By.CSS_SELECTOR, "._3sKvP.wQZ0F ._274yw div.copyable-text ._3Whw5 span")
    CHAT_BODY_MSG_ARROW = (By.CSS_SELECTOR, "._2nBjH._1q11a ._2oA--")
    # -> THIS ARE OUT OF THE CONTEXT OF THE HTML ELEMENT.
    CHAT_BODY_MSG_ARROW_POP_MENU = (By.CSS_SELECTOR, "._2s_eZ")
    CHAT_BODY_MSG_ARROW_POP_MENU_REPLY = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(1) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_FORWARD = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(2) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_STAR = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(3) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_DELETE = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(4) div")
    # <- END
    CHAT_BODY_UNREAD_MESSAGE = (By.CSS_SELECTOR, "._9WQEN")
    CHAT_BODY_ARROW_BUTTON = (By.CSS_SELECTOR, "._1YcH-._1-MYr")
    CHAT_BODY_ARROW_BUTTON_NOTIFICATION_QTY = (By.CSS_SELECTOR, "._31gEB")

    # SENDING MSGS
    CHAT_FOOTER = (By.CSS_SELECTOR, "#main footer")
    CHAT_FOOTER_SMILEY_ICON = (By.CSS_SELECTOR, "#main footer ._2X5R7")
    CHAT_FOOTER_TEXT_INPUT_FIELD = (By.CSS_SELECTOR, "#main footer ._3FRCZ")
    CHAT_FOOTER_RECORD_ICON = (By.CSS_SELECTOR, "#main footer ._2r1fJ")


class WelcomeLocators(object):
    WELCOME = (By.CSS_SELECTOR, "._1kdBg")
