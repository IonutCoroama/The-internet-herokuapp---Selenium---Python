from selenium.webdriver.common.by import By
from utils.constants import Constants
from utils.generic_methods import GenericMethods


class SecureAreaPage:
    const = Constants
    URL = const.SECURE_AREA_URL
    TITLE_TEXT = (By.CSS_SELECTOR, 'h2')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '*.button')
    LOGIN_MESSAGE = const.FLASH_MESSAGE

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        generic = GenericMethods(self.browser)
        generic.login_valid_account()

    def get_title_text(self):
        return self.browser.find_element(*self.TITLE_TEXT).text

    def is_logout_button_displayed(self):
        return self.browser.find_element(*self.LOGOUT_BUTTON).is_displayed()

    def is_login_successful_message_displayed(self):
        const = Constants
        return const.SUCCESS_LOGOUT_MESSGE in self.browser.find_element(*self.LOGIN_MESSAGE).text

    def click_logout_button(self):
        self.browser.find_element(*self.LOGOUT_BUTTON).click()
