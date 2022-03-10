from selenium.webdriver.common.by import By
from utils.constants import Constants


class LoginPage:
    const = Constants
    URL = const.FORM_AUTHENTICATION_URL
    TITLE_TEXT = (By.CSS_SELECTOR, 'h2')
    USERNAME_FIELD = (By.CSS_SELECTOR, '#username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type = "submit"]')
    FLASH_MESSAGE = const.FLASH_MESSAGE

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_title_text(self):
        return self.browser.find_element(*self.TITLE_TEXT).text

    def is_login_button_displayed(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()

    def is_username_field_displayed(self):
        return self.browser.find_element(*self.USERNAME_FIELD).is_displayed()

    def is_password_field_displayed(self):
        return self.browser.find_element(*self.PASSWORD_FIELD).is_displayed()

    def type_username(self, user):
        self.browser.find_element(*self.USERNAME_FIELD).send_keys(user)

    def type_password(self, password):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def is_login_successful_message_displayed(self):
        const = Constants
        return const.SUCCESS_LOGIN_MESSAGE in self.browser.find_element(*self.FLASH_MESSAGE).text

    def is_logout_successful_message_displayed(self):
        const = Constants
        return const.SUCCESS_LOGOUT_MESSGE in self.browser.find_element(*self.FLASH_MESSAGE).text

    def is_invalid_username_message_displayed(self):
        const = Constants
        return const.INVALID_USER_MESSAGE in self.browser.find_element(*self.FLASH_MESSAGE).text

    def is_invalid_password_message_displayed(self):
        const = Constants
        return const.INVALID_PASSWORD_MESSAGE in self.browser.find_element(*self.FLASH_MESSAGE).text

    def login_procedure(self, user, password):
        self.type_username(user)
        self.type_password(password)
        self.click_login_button()
