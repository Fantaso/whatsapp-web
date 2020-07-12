from selenium.webdriver.common.by import By


class NavBarLocators(object):
    # parent
    BAR = (By.CSS_SELECTOR, "._1QUKR")
    # childs
    BAR_PROFILE = (By.CSS_SELECTOR, "._1MXsz ._3Whw5")
    BAR_STATUS = (By.CSS_SELECTOR, ".PVMjB:nth-child(1)")
    BAR_NEW_CHAT = (By.CSS_SELECTOR, ".PVMjB:nth-child(2)")
    BAR_MENU = (By.CSS_SELECTOR, ".PVMjB:nth-child(3)")
