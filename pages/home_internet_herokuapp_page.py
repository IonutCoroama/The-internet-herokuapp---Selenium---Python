from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HomePage:

    # URl
    URL = "https://the-internet.herokuapp.com/"

    # locators
    HEADING_TEXT = (By.CSS_SELECTOR, "h1")
    TITLE_TEXT = (By.CSS_SELECTOR, "h2")
    AB_TEST_LINK = (By.CSS_SELECTOR, "a[href = '/abtest']")
    ADD_REMOVE_ELEMENTS_LINK = (By.CSS_SELECTOR, 'a[href="/add_remove_elements/"]')
    BROKEN_IMAGES_LINK = (By.CSS_SELECTOR, 'a[href="/broken_images"]')
    FORM_AUTHENTICATION_LINK = (By.CSS_SELECTOR, 'a[href="/login"]')
    FOOTER = (By.CLASS_NAME, 'large-4')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_heading_text(self):
        return self.browser.find_element(*self.HEADING_TEXT).text

    def get_title_text(self):
        return self.browser.find_element(*self.TITLE_TEXT).text

    def click_a_b_test_link(self):
        self.browser.find_element(*self.AB_TEST_LINK).click()

    def is_a_b_test_link_displayed(self):
        return self.browser.find_element(*self.AB_TEST_LINK).is_displayed()

    def is_add_remove_elements_link_displayed(self):
        return self.browser.find_element(*self.ADD_REMOVE_ELEMENTS_LINK).is_displayed()

    def click_add_remove_elements_link(self):
        self.browser.find_element(*self.ADD_REMOVE_ELEMENTS_LINK).click()

    def is_broken_images_link_displayed(self):
        return self.browser.find_element(*self.BROKEN_IMAGES_LINK).is_displayed()

    def click_broken_images_link(self):
        self.browser.find_element(*self.BROKEN_IMAGES_LINK).click()

    def is_form_authentication_link_displayed(self):
        return self.browser.find_element(*self.FORM_AUTHENTICATION_LINK).is_displayed()

    def click_form_authentication_link(self):
        self.browser.find_element(*self.FORM_AUTHENTICATION_LINK).click()

    def is_heading_text_displayed(self):
        return self.browser.find_element(*self.HEADING_TEXT).is_displayed()

    def is_title_text_displayed(self):
        return self.browser.find_element(*self.TITLE_TEXT).is_displayed()

    def is_footer_displayed(self):
        return self.browser.find_element(*self.FOOTER).is_displayed()

    def scroll_to_footer(self):
        footer = self.browser.find_element(*self.FOOTER)
        action = ActionChains(self.browser)
        action.move_to_element(footer).perform()

    def scroll_to_header(self):
        heading = self.browser.find_element(*self.HEADING_TEXT)
        action = ActionChains(self.browser)
        action.move_to_element(heading).perform()

    def click_link(self, link):
        if link == 'ab_test_link':
            self.click_a_b_test_link()
        elif link == 'add_remove_elements_link':
            self.click_add_remove_elements_link()
        elif link == 'broken_images_link':
            self.click_broken_images_link()
        elif link == 'form_authentication_link':
            self.click_form_authentication_link()
        else:
            print('I did not code any action for this value')


