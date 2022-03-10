from selenium.webdriver.common.by import By


class BrokenImagesPage:
    URL = "https://the-internet.herokuapp.com/broken_images"
    TITLE_TEXT = (By.CSS_SELECTOR, 'h3')
    FIRST_IMAGE = (By.CSS_SELECTOR, '.example > img:nth-child(2)')
    SECOND_IMAGE = (By.CSS_SELECTOR, '.example > img:nth-child(3)')
    THIRD_IMAGE = (By.CSS_SELECTOR, '.example > img:nth-child(4)')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_title_text(self):
        return self.browser.find_element(*self.TITLE_TEXT).text

    def is_first_image_visible(self):
        return self.browser.find_element(*self.FIRST_IMAGE).is_displayed()

    def is_second_image_visible(self):
        return self.browser.find_element(*self.SECOND_IMAGE).is_displayed()

    def is_third_image_visible(self):
        return self.browser.find_element(*self.THIRD_IMAGE).is_displayed()
