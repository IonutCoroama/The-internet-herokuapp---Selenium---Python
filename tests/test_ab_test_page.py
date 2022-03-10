from pages.ab_test_page import AbTestingPage
from utils.generic_methods import GenericMethods


def test_page_is_displayed(browser):
    print('''   Scenario: Test if the A/B Test page is displayed if I launch the page 10 times in a row
    Given I type "https://the-internet.herokuapp.com/abtest" in the Chrome address-bar
    When I launch the page
    Then the page should open
    and the Title text should be visible and displaying the correct text''')
    a_b_testing_page = AbTestingPage(browser)
    a_b_testing_page.load_page()
    for i in range(10):
        a_b_testing_page.load_page()
        print(a_b_testing_page.get_title_text())
        assert "A/B Test" in a_b_testing_page.get_title_text(), "AB test page is not displayed correct"
        browser.back()

def test_broken_images(browser):
    print('''   Scenario: Test if in the A/B Test page there are some broken images 
        Given I type "https://the-internet.herokuapp.com/abtest" in the Chrome address-bar
        When I launch the page
        and verify if in the page are some broken images
        Then I should not find any broken images''')
    a_b_testing_page = AbTestingPage(browser)
    a_b_testing_page.load_page()
    generic = GenericMethods(browser)
    assert generic.is_broken_images_on_page(), 'The page contains broken images'
