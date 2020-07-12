from selenium.webdriver.common.by import By


class HeaderLocators(object):
    HEADER = (By.CSS_SELECTOR, "._1QUKR")

    HEADER_PROFILE = (By.CSS_SELECTOR, "._1MXsz ._3Whw5")
    HEADER_STATUS = (By.CSS_SELECTOR, ".PVMjB:nth-child(1)")
    HEADER_NEW_CHAT = (By.CSS_SELECTOR, ".PVMjB:nth-child(2)")

    HEADER_MENU = (By.CSS_SELECTOR, ".PVMjB:nth-child(3)")
    HEADER_MENU_POP_MENU = (By.CSS_SELECTOR, ".PVMjB:nth-child(3) .I4jbF")
    HEADER_MENU_POP_MENU_CREATE_GROUP = (By.CSS_SELECTOR, ".PVMjB:nth-child(3) .I4jbF li:nth-child(1) div")
    HEADER_MENU_POP_MENU_CREATE_ROOM = (By.CSS_SELECTOR, ".PVMjB:nth-child(3) .I4jbF li:nth-child(2) div")
    HEADER_MENU_POP_MENU_PROFILE = (By.CSS_SELECTOR, ".PVMjB:nth-child(3) .I4jbF li:nth-child(3) div")
    HEADER_MENU_POP_MENU_ARCHIVED = (By.CSS_SELECTOR, ".PVMjB:nth-child(3) .I4jbF li:nth-child(4) div")
    HEADER_MENU_POP_MENU_STARRED = (By.CSS_SELECTOR, ".PVMjB:nth-child(3) .I4jbF li:nth-child(5) div")
    HEADER_MENU_POP_MENU_SETTINGS = (By.CSS_SELECTOR, ".PVMjB:nth-child(3) .I4jbF li:nth-child(6) div")
    HEADER_MENU_POP_MENU_LOGOUT = (By.CSS_SELECTOR, ".PVMjB:nth-child(3) .I4jbF li:nth-child(7) div")
