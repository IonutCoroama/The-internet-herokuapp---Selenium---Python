from pages.broken_images_page import BrokenImagesPage
from utils.generic_methods import GenericMethods


def test_page_is_displayed(browser):
    print('''   Scenario: Test if the Broken Images page is displayed
    Given I type "https://the-internet.herokuapp.com/broken_images" in the Chrome address-bar
    When I launch the page
    Then the page should open
    and the Title text should be visible and displaying the correct text
    and 3 images should be displayed''')
    broken_images_page = BrokenImagesPage(browser)
    broken_images_page.load_page()
    assert broken_images_page.get_title_text() == "Broken Images", "The title is not displayed OK"
    assert broken_images_page.is_first_image_visible()
    assert broken_images_page.is_second_image_visible()
    assert broken_images_page.is_third_image_visible()


def test_broken_images(browser):
    print('''   Scenario: Test if in the Broken Images page there are some broken images 
        Given I launch the page "https://the-internet.herokuapp.com/broken_images" in the Chrome browser
        When I verify if in the page are some broken images
        Then I should not find any broken images''')
    broken_images_page = BrokenImagesPage(browser)
    broken_images_page.load_page()
    generic = GenericMethods(browser)
    assert generic.is_broken_images_on_page(), 'The page contains broken images'
