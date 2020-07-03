from selenium.webdriver.common.by import By


class ChatLocators(object):
    CHAT_SECTION = (By.CSS_SELECTOR, "#main")
    # chat nav bar
    CHAT_HEADER = (By.CSS_SELECTOR, "#main header")
    # messages space
    CHAT_BODY = (By.CSS_SELECTOR, "#main ._2-aNW .z_tTQ")

    MSGS_IN = (By.CSS_SELECTOR, "#main ._2-aNW .z_tTQ ._2hqOq.message-in ._274yw")
    MSG_IN_TEXT = (By.CSS_SELECTOR, "#main ._2-aNW .z_tTQ ._2hqOq.message-in ._274yw ._3Whw5")
    MSG_IN_TIME = (By.CSS_SELECTOR, "#main ._2-aNW .z_tTQ ._2hqOq.message-in ._274yw ._18lLQ")

    MSGS_OUT = (By.CSS_SELECTOR, "#main ._2-aNW .z_tTQ ._2hqOq.message-out ._274yw")
    MSG_OUT_TEXT = (By.CSS_SELECTOR, "#main ._2-aNW .z_tTQ ._2hqOq.message-out ._274yw ._3Whw5")
    MSG_OUT_TIME = (By.CSS_SELECTOR, "#main ._2-aNW .z_tTQ ._2hqOq.message-out ._274yw ._2frDn ._18lLQ")
    MSG_OUT_ARROW = (By.CSS_SELECTOR, "#main ._2-aNW .z_tTQ ._2hqOq.message-out ._274yw ._2frDn ._1qPwk")

    DATES_SEPARATION = (By.CSS_SELECTOR, "#main ._2-aNW .z_tTQ ._2hqOq._2qhWD")

    # write messages
    CHAT_FOOTER = (By.CSS_SELECTOR, "#main footer")
    SMILEY_ICON = (By.CSS_SELECTOR, "#main footer ._2X5R7")
    TEXT_FIELD = (By.CSS_SELECTOR, "#main footer ._3FRCZ")
    RECORD_ICON = (By.CSS_SELECTOR, "#main footer ._2r1fJ")


# Page - Left side
class ProfileLocators(object):
    PROFILE_BAR = (By.CLASS_NAME, "._1QUKR")
    PROFILE = (By.CSS_SELECTOR, "._1MXsz ._3Whw5")
    STATUS = (By.CSS_SELECTOR, ".PVMjB:nth-child(1)")
    NEW_CHAT = (By.CSS_SELECTOR, ".PVMjB:nth-child(2)")
    MENU = (By.CSS_SELECTOR, ".PVMjB:nth-child(3)")

    # SearchLocators:
    # SEARCH = (,)
    # CHATS = (,)
    # GROUPS = (,)
    # CONTACTS = (,)  # creating a new chat
    # MESSAGES = (,)

    # PanePageLocators
    PANE_SECTION = (By.CSS_SELECTOR, "#pane-side")
    OPENED_CHATS = (By.CSS_SELECTOR, "#pane-side ._210SC")
    ## left side
    CONTACT_ICONS = (By.CSS_SELECTOR, "#pane-side ._210SC ._1BjNO")
    ## right side
    ### upper side
    CONTACT_NAMES = (By.CSS_SELECTOR, "#pane-side ._3dtfX ._357i8 ._3ko75")
    LAST_MSG_TIMES = (By.CSS_SELECTOR, "#pane-side ._3dtfX .m61XR")
    ### bottom side
    ARROW_STATUSES = (By.CSS_SELECTOR, "#pane-side ._210SC ._1582E .zFnXi")
    TRUNCATED_MSGS = (By.CSS_SELECTOR, "#pane-side ._210SC ._1582E ._2iq-U span._3ko75")
    NEW_MESSAGE_ICONS = (By.CSS_SELECTOR, "#pane-side ._210SC ._1582E .m61XR .ZKn2B ._31gEB")
