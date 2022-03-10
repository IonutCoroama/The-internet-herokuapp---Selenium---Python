import time
from selenium.webdriver.common.by import By
import requests
from utils.constants import Constants
from pages.form_authentication_page import LoginPage
import random
import string


class GenericMethods:
    def __init__(self, browser):
        self.browser = browser

    def load_page(self, URL):
        self.browser.get(URL)

    def get_current_url(self):
        return self.browser.current_url

    def is_broken_images_on_page(self):
        image_list = self.browser.find_elements(By.TAG_NAME, "img")
        broken_images_list = []
        counter = 0
        for i in image_list:
            response = requests.get(i.get_attribute('src'), stream=True)
            if response.status_code != 200:
                broken_images_list.append(i.get_attribute("outerHTML"))
                counter += 1
        print(f'            This page contains: {len(image_list)} images')
        print(f'    Broken images: \n{broken_images_list}')
        if counter:
            return False
        else:
            return True

    def print_flash_message(self):
        const = Constants
        print(f'        Flash message: {self.browser.find_element(*const.FLASH_MESSAGE).text}')

    def login_valid_account(self):
        login_page = LoginPage(self.browser)
        const = Constants
        login_page.load_page()
        login_page.login_procedure(const.VALID_USERNAME, const.VALID_PASSWORD)


    def generate_password_length(self):
        choice = []
        for i in range(9999):
            choice.append(i)
        return random.randrange(8, 16)


    def generate_password(self):
        special_characters = "!@#$%^&*()_+=-}{][|:;'<>,.?/"
        specials_list = []
        for i in special_characters:
            specials_list.append(i)
        digits_list = []
        for i in range(10):
            digits_list.append(str(i))
        letters_list = list(string.ascii_letters)
        characters = specials_list + digits_list + letters_list
        random.shuffle(characters)
        generated_password_list = []
        password_length = self.generate_password_length()
        for i in range(password_length):
            generated_password_list.append(random.choice(characters))
        random.shuffle(generated_password_list)
        generated_password = ''.join(generated_password_list)
        # generated_password.join(generated_password_list)
        # print(password_length)
        # print(f'Generated password: {generated_password}')
        return generated_password


    def generate_username(self):
        generated_username_list = []
        letters_list = list(string.ascii_letters)
        random.shuffle(letters_list)
        username_length = self.generate_password_length()
        for i in range(username_length):
            generated_username_list.append(random.choice(letters_list))
        random.shuffle(generated_username_list)
        generated_username = ''.join(generated_username_list)
        print(username_length)
        print(f'Generated usermane: {generated_username}')
        return generated_username