from selenium.webdriver.common.by import By


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
    # all
    CHAT_BODY_MSGS = (By.CSS_SELECTOR, "._2hqOq.message-in, ._2hqOq.message-out")
    # filtered by "contact"
    CHAT_BODY_MSGS_MYSELF = (By.CSS_SELECTOR, "._2hqOq.message-out")
    CHAT_BODY_MSGS_CONTACT = (By.CSS_SELECTOR, "._2hqOq.message-in")
    # filtered by "type"
    CHAT_BODY_MSGS_TYPE_VOICE_RECORDING = (By.CSS_SELECTOR, "._3D5PJ")
    CHAT_BODY_MSGS_TYPE_VIDEO = (By.CSS_SELECTOR, ".S9d8c")
    CHAT_BODY_MSGS_TYPE_IMAGE = (By.CSS_SELECTOR, ".xOg_4")
    CHAT_BODY_MSGS_TYPE_GIFF = (By.CSS_SELECTOR, "._3gBQS")
    CHAT_BODY_MSGS_TYPE_AUDIO = (By.CSS_SELECTOR, "")

    # message details
    CHAT_BODY_MSG_CONTACT_AND_DATETIME = (By.CSS_SELECTOR, "._3sKvP.wQZ0F ._274yw div.copyable-text")
    CHAT_BODY_MSG_STATUS = (By.CSS_SELECTOR, "._3sKvP.wQZ0F ._274yw div._2frDn ._1qPwk span")
    CHAT_BODY_MSG_TEXT = (By.CSS_SELECTOR, "._3sKvP.wQZ0F ._274yw div.copyable-text ._3Whw5 span")
    CHAT_BODY_MSG_ARROW_MY_OWN_MSG = (By.CSS_SELECTOR, "._4tndQ._1q11a ._2oA--")
    CHAT_BODY_MSG_ARROW = (By.CSS_SELECTOR, "._2nBjH._1q11a ._2oA--")

    # -> THIS ARE OUT OF THE CONTEXT OF THE HTML ELEMENT.
    CHAT_BODY_MSG_ARROW_POP_MENU = (By.CSS_SELECTOR, "._2s_eZ")
    CHAT_BODY_MSG_ARROW_POP_MENU_REPLY = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(1) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_FORWARD = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(2) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_STAR = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(3) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_DELETE = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(4) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_MY_OWN_MSG_MSG_INFO = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(1) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_MY_OWN_MSG_REPLY = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(2) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_MY_OWN_MSG_FORWARD = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(3) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_MY_OWN_MSG_STAR = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(4) div")
    CHAT_BODY_MSG_ARROW_POP_MENU_MY_OWN_MSG_DELETE = (By.CSS_SELECTOR, "._2s_eZ ._1N-3y.eP_pD._36Osw:nth-child(5) div")
    # <- END
    CHAT_BODY_UNREAD_MESSAGE = (By.CSS_SELECTOR, "._9WQEN")
    CHAT_BODY_ARROW_BUTTON = (By.CSS_SELECTOR, "._1YcH-._1-MYr")
    CHAT_BODY_ARROW_BUTTON_NOTIFICATION_QTY = (By.CSS_SELECTOR, "._31gEB")

    # SENDING MSGS
    CHAT_FOOTER = (By.CSS_SELECTOR, "#main footer")
    CHAT_FOOTER_SMILEY_ICON = (By.CSS_SELECTOR, "#main footer ._2X5R7")
    CHAT_FOOTER_TEXT_INPUT_FIELD = (By.CSS_SELECTOR, "#main footer ._3FRCZ")
    CHAT_FOOTER_RECORD_ICON = (By.CSS_SELECTOR, "#main footer ._2r1fJ")
