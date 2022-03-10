from pages.secure_area_page import SecureAreaPage
from pages.form_authentication_page import LoginPage
from utils.generic_methods import GenericMethods
from utils.constants import Constants


def test_logout_page_is_displayed(browser):
    print('''   Scenario: Test if the Secure Area page is displayed
    Given I type "https://the-internet.herokuapp.com/login" in the Chrome address-bar
    When I successfully login
    Then the Secure Area page should open
    and a flash message should appear to confirm the successful login
    and the Title text should be visible and displaying the correct text
    and the Logout button should be displayed''')
    generic = GenericMethods(browser)
    login_page = LoginPage(browser)
    secure_page = SecureAreaPage(browser)
    secure_page.load_page()
    assert secure_page.get_title_text() == 'Secure Area', 'Title text is not OK'
    assert secure_page.is_logout_button_displayed(), 'Logout button is not displayed'
    generic.print_flash_message()
    assert login_page.is_login_successful_message_displayed(), 'Successful login message is not displayed'


def test_logout(browser):
    print('''   Scenario: Test if the logout from the Secure Area page is working
    Given I'm successfully logged in 
    When I click Logout button
    Then the Login page should open
    and a flash message should appear to confirm the successful logout''')
    secure_page = SecureAreaPage(browser)
    secure_page.load_page()
    const = Constants
    login_page = LoginPage(browser)
    generic = GenericMethods(browser)
    secure_page.click_logout_button()
    assert generic.get_current_url() == const.FORM_AUTHENTICATION_URL
    generic.print_flash_message()
    assert login_page.is_logout_successful_message_displayed(), "Successful logout message not OK"


def test_go_back_after_logout(browser):
    print('''   Scenario: Test if the logout functionality is secure
    Given I'm successfully logged in 
    and I click Logout button
    and after the login page is displayed
    When I navigate backward using the Back button from the browser
    Then the browser should remain in the login page
    and should ask me to login again''')
    secure_page = SecureAreaPage(browser)
    secure_page.load_page()
    generic = GenericMethods(browser)
    secure_page_url = generic.get_current_url()
    secure_page.click_logout_button()
    browser.back()
    assert generic.get_current_url() is secure_page_url, \
        'Unsecure logout: If we go back after logout, we are logged in back'
