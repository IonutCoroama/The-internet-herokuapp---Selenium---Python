
from selenium.webdriver.common.by import By


class AddRemoveElementsPage:

    # URl
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    # locators
    TITLE_TEXT = (By.CSS_SELECTOR, "h3")
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[onclick='deleteElement()']")

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_title_text(self):
        return self.browser.find_element(*self.TITLE_TEXT).text

    def click_add_element_button(self):
        self.browser.find_element(*self.ADD_ELEMENT_BUTTON).click()

    def click_delete_button(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    def is_add_element_button_displayed(self):
        return self.browser.find_element(*self.ADD_ELEMENT_BUTTON).is_displayed()

    def is_delete_element_button_displayed(self):
        return self.browser.find_element(*self.DELETE_BUTTON).is_displayed()

    def get_number_of_delete_buttons(self):
        return len(self.browser.find_elements(*self.DELETE_BUTTON))
