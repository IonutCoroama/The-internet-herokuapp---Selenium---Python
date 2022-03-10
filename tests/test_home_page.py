from pages.home_internet_herokuapp_page import HomePage
from utils.constants import Constants
from utils.generic_methods import GenericMethods


def test_page_is_displayed(browser):
    print('''   Scenario: Test if the the-internet.herokuapp.com page is displayed 
        Given I type "https://the-internet.herokuapp.com/" in the Chrome address-bar
        When I launch the page
        Then the page should open
        and the Header text should be visible and containing the correct text
        and the Title text should be visible and containing the correct text
        and if I scroll to the bottom of the page I should see the footer''')
    home_page = HomePage(browser)
    home_page.load_page()
    assert home_page.is_heading_text_displayed(), 'Header is not displayed'
    assert home_page.is_title_text_displayed(), 'Title is not displayed'
    assert home_page.get_heading_text() == "Welcome to the-internet", "Heading text don\'t mach"
    assert home_page.get_title_text() == 'Available Examples', "Title text don\'t mach"
    home_page.scroll_to_footer()
    assert home_page.is_footer_displayed(), 'Footer is not displayed'
    home_page.scroll_to_header()


def test_links_are_displayed(browser):
    print('''   Scenario: Test if in the the-internet.herokuapp.com page, the correct links is displayed 
        mGiven I type "https://the-internet.herokuapp.com/" in the Chrome address-bar
        When I launch the page
        Then the page should open
        and I should see the A/B Testing, Add/Remove Elements, 
        Broken Images and Form Authentication links displayed''')
    home_page = HomePage(browser)
    home_page.load_page()
    assert home_page.is_a_b_test_link_displayed(), 'A/B Testing link is not displayed'
    assert home_page.is_add_remove_elements_link_displayed(), 'Add/Remove Elements link is not displayed'
    assert home_page.is_broken_images_link_displayed(), 'Broken Images link is not displayed'
    assert home_page.is_form_authentication_link_displayed(), 'Form Authentication link is not displayed'


def test_links_are_working(browser):
    print('''   Scenario: Test if in the the-internet.herokuapp.com page the links are working 
        Given I type "https://the-internet.herokuapp.com/" in the Chrome address-bar
        When I launch the page
        Then the page should open
        and the links A/B Testing, Add/Remove Elements, 
        Broken Images and Form Authentication should be clickable
        and if I click them I should be redirected to the correct target page''')
    home_page = HomePage(browser)
    home_page.load_page()
    const = Constants
    generic = GenericMethods(browser)
    print(generic.get_current_url())
    home_page.click_a_b_test_link()
    print(generic.get_current_url())
    assert generic.get_current_url() == const.AB_TEST_URL, 'AB test link is not OK'
    browser.back()
    print(generic.get_current_url())
    home_page.click_broken_images_link()
    print(generic.get_current_url())
    assert generic.get_current_url() == const.BROKEN_IMAGES_URL, 'Broken images link is not OK'
    browser.back()
    print(generic.get_current_url())
    home_page.click_add_remove_elements_link()
    print(generic.get_current_url())
    assert generic.get_current_url() == const.ADD_REMOVE_ELEMENTS_URL, 'Add remove elements link is not OK'
    browser.back()
    print(generic.get_current_url())
    home_page.click_form_authentication_link()
    print(generic.get_current_url())
    assert generic.get_current_url() == const.FORM_AUTHENTICATION_URL, 'Form authentication link is not OK'
    browser.back()
    print(generic.get_current_url())
    assert generic.get_current_url() == const.HOME_PAGE_URL, 'We have to return to home page when back is pushed'


def test_broken_images(browser):
    print('''   Scenario: Test if in the the-internet.herokuapp.com page there are some broken images 
        Given I type "https://the-internet.herokuapp.com/" in the Chrome address-bar
        When I launch the page
        and verify if in the page are some broken images
        Then I should not find any broken images''')
    home_page = HomePage(browser)
    home_page.load_page()
    generic = GenericMethods(browser)
    assert generic.is_broken_images_on_page(), 'The page contains broken images'
