from selenium.webdriver.common.by import By
from utils.constants import Constants


class AbTestingPage:
    const = Constants
    URL = const.AB_TEST_URL
    TITLE_TEXT = (By.CSS_SELECTOR, 'h3')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_title_text(self):
        return self.browser.find_element(*self.TITLE_TEXT).text
