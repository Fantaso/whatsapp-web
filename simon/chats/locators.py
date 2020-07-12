from selenium.webdriver.common.by import By


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
