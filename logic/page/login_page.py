import logging
import time
from selenium import webdriver
from logic.page.basic_page import BasicPage
from typing import Dict, Tuple
from selenium.webdriver.common.by import By
from logic.page.my_account_page import MyAccountPage


class LoginPage(BasicPage):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def do_login(self, email: str, password: str,  logger: logging.Logger) -> MyAccountPage:
        logger.info("entering the email")
        print("entering the email")
        self.find_element_and_color_it(*self.locator_dictionary['email_textbox']).send_keys(email)
        time.sleep(1)
        logger.info("entering the password")
        print("entering the password")
        self.find_element_and_color_it(*self.locator_dictionary['password_textbox']).send_keys(password)
        time.sleep(1)

        # Click on submit
        self.find_element_and_color_it(*self.locator_dictionary['submit_login_button']).click()
        logger.info("Submit login button was clicked")
        print("Submit login button was clicked")
        return MyAccountPage(self.driver)

    locator_dictionary: Dict[str, Tuple[str, str]] = {
        "email_textbox": (By.ID, "email"),
        "password_textbox": (By.ID, "passwd"),
        "submit_login_button": (By.ID, "SubmitLogin")
    }

