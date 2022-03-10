import time

from pages.form_authentication_page import LoginPage
from utils.generic_methods import GenericMethods
from utils.constants import Constants


def test_page_is_displayed(browser):
    print('''   Scenario: Test if the Form Authentication page is displayed
    Given I type "https://the-internet.herokuapp.com/login" in the Chrome address-bar
    When I launch the page
    Then the page should open
    and the Title text should be visible and displaying the correct text
    and the username field should appear
    and the password field should appear
    and the Login button should be displayed''')
    login_page = LoginPage(browser)
    login_page.load_page()
    assert login_page.get_title_text() == "Login Page", 'Page title is not OK'
    assert login_page.is_username_field_displayed(), 'Username field is not displayed'
    assert login_page.is_password_field_displayed(), 'Password field is not displayed'
    assert login_page.is_login_button_displayed(), 'Login button is not displayed'


def test_login_with_valid_credentials(browser):
    print('''   Scenario: Test Login with valid credentials
    Given I launch the "https://the-internet.herokuapp.com/login" page in the Chrome address-bar
    When I type the correct username
    and I type the correct password
    and I click the Login button
    Then the secure page should open
    and a flash message should appear to confirm the successful login''')
    login_page = LoginPage(browser)
    login_page.load_page()
    generic = GenericMethods(browser)
    const = Constants
    login_page.login_procedure(const.VALID_USERNAME, const.VALID_PASSWORD)
    assert generic.get_current_url() == const.SECURE_AREA_URL
    generic.print_flash_message()
    assert login_page.is_login_successful_message_displayed(), "Successful login message not OK"


def test_login_with_invalid_password(browser):
    print('''   Scenario: Test Login with valid username and invalid password
    Given I launch the "https://the-internet.herokuapp.com/login" page in the Chrome address-bar
    When I type the correct username
    and I type an incorrect password
    and I click the Login button
    Then the borwser should still display the login page
    and a flash message should appear to warn me that I entered an incorrect password''')
    generic = GenericMethods(browser)
    login_page = LoginPage(browser)
    login_page.load_page()
    const = Constants
    invalid_password_list = []
    for i in range(10):
        invalid_password_list.append(generic.generate_password())
    print(invalid_password_list)
    for password in invalid_password_list:
        print(password)
        login_page.login_procedure(const.VALID_USERNAME, password)
        time.sleep(1)
        print(generic.get_current_url())
        assert generic.get_current_url() == const.FORM_AUTHENTICATION_URL, 'Unexpected redirect from login page'
        print(generic.print_flash_message())
        assert login_page.is_invalid_password_message_displayed(), 'Invalid password alert is not displayed'
        time.sleep(1)

def test_login_with_invalid_username(browser):
    print('''   Scenario: Test Login with invalid credentials
    Given I launch the "https://the-internet.herokuapp.com/login" page in the Chrome address-bar
    When I type a random invalid username
    and I type an random invalid password
    and I click the Login button
    Then the borwser should still display the login page
    and a flash message should appear to warn me that I entered an incorrect username''')
    generic = GenericMethods(browser)
    login_page = LoginPage(browser)
    login_page.load_page()
    const = Constants
    invalid_password_list = []
    invalid_username_list = []
    for i in range(10):
        invalid_password_list.append(generic.generate_password())
        invalid_username_list.append(generic.generate_username())

    for i in range(len(invalid_password_list)):
        print(invalid_username_list[i])
        print(invalid_password_list[i])
        login_page.login_procedure(invalid_username_list[i], invalid_password_list[i])
        time.sleep(1)
        print(generic.get_current_url())
        assert generic.get_current_url() == const.FORM_AUTHENTICATION_URL, 'Unexpected redirect from login page'
        print(generic.print_flash_message())
        assert login_page.is_invalid_username_message_displayed(), 'Invalid username alert is not displayed or the username exists'
        time.sleep(1)
