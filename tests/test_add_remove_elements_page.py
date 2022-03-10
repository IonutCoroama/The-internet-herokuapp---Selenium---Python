from pages.add_remove_elements_page import AddRemoveElementsPage
from utils.generic_methods import GenericMethods


def test_page_is_displayed(browser):
    print('''   Scenario: Test if the Add Remove Elements page is displayed 
        Given I type "https://the-internet.herokuapp.com/add_remove_elements/" in the Chrome address-bar
        When I launch the page
        Then the page should open
        and the Title text should be visible and displaying the correct text
        and the Add Element button should be displayed''')
    add_remove_elements_page = AddRemoveElementsPage(browser)
    add_remove_elements_page.load_page()
    assert add_remove_elements_page.get_title_text() == "Add/Remove Elements", "Title is not OK"
    assert add_remove_elements_page.is_add_element_button_displayed(), "Add/Remove Elements button is not displayed"


def test_buttons_works(browser):
    print('''   Scenario: Test if the Add Remove Elements page is displayed 
        Given I launch the page "https://the-internet.herokuapp.com/add_remove_elements/" in the Chrome browser
        When I click the Add Element button once
        Then one Delete button should appear
        and When I click the Delete button once
        Then the clicked Delete button should disappear''')
    add_remove_elements_page = AddRemoveElementsPage(browser)
    add_remove_elements_page.load_page()
    add_remove_elements_page.click_add_element_button()
    assert add_remove_elements_page.is_delete_element_button_displayed(), "Delete button is not displayed"
    add_remove_elements_page.click_delete_button()
    assert add_remove_elements_page.get_number_of_delete_buttons() == 0, \
        "Delete button is still displayed after it's pushed"


def test_delete_buttons_number(browser):
    print('''   Scenario: Test if in the Add Remove Elements page the number of delete buttons are the same 
        with the number of times I clicked the Add Element button 
        Given I launch the page "https://the-internet.herokuapp.com/add_remove_elements/" in the Chrome browser
        When I click the Add Element button certain number of times
        Then the number of Delete buttons displayed on the page should be the same 
        with the number of times I clicked the Add Element Button
        and When I click the Delete button several times
        Then the clicked Delete buttons should disappear''')
    add_remove_elements_page = AddRemoveElementsPage(browser)
    add_remove_elements_page.load_page()
    for i in range(50):
        add_remove_elements_page.click_add_element_button()
        assert add_remove_elements_page.get_number_of_delete_buttons() == i + 1, "Delete buttons number is not OK"
    n = add_remove_elements_page.get_number_of_delete_buttons()
    for i in range(1, n + 1):
        add_remove_elements_page.click_delete_button()
        assert add_remove_elements_page.get_number_of_delete_buttons() == n - i, "Delete buttons number is not OK"


def test_broken_images(browser):
    print('''   Scenario: Test if in the Add Remove Elements page there are some broken images 
        Given I launch the page "https://the-internet.herokuapp.com/add_remove_elements/" in the Chrome browser
        When I verify if in the page are some broken images
        Then I should not find any broken images''')
    add_remove_elements_page = AddRemoveElementsPage(browser)
    add_remove_elements_page.load_page()
    generic = GenericMethods(browser)
    assert generic.is_broken_images_on_page(), 'The page contains broken images'
