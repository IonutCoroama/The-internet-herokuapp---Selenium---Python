from selenium.webdriver.common.by import By


class Constants:
    HOME_PAGE_URL = "https://the-internet.herokuapp.com/"
    AB_TEST_URL = "https://the-internet.herokuapp.com/abtest"
    ADD_REMOVE_ELEMENTS_URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    BROKEN_IMAGES_URL = "https://the-internet.herokuapp.com/broken_images"
    FORM_AUTHENTICATION_URL = "https://the-internet.herokuapp.com/login"
    SECURE_AREA_URL = "https://the-internet.herokuapp.com/secure"
    VALID_USERNAME = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"
    FLASH_MESSAGE = (By.CSS_SELECTOR, '#flash')
    SUCCESS_LOGIN_MESSAGE = 'You logged into a secure area!'
    INVALID_USER_MESSAGE = 'Your username is invalid!'
    INVALID_PASSWORD_MESSAGE = 'Your password is invalid!'
    SUCCESS_LOGOUT_MESSGE = 'You logged out of the secure area!'


    def __init__(self, const):
        self.const = const
