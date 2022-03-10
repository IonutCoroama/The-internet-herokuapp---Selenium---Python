import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()
