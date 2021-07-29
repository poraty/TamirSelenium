from selenium import webdriver
from logic.page.basic_page import BasicPage
import logging
from typing import Dict, Tuple
from selenium.webdriver.common.by import By
# from logic.page.main_page import MainPage


class MyAccountPage(BasicPage):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def click_on_home_button(self, logger: logging.Logger):
    # def click_on_home_button(self, logger: logging.Logger) -> MainPage:
        self.find_element_and_color_it(*self.locator_dictionary['home_btn']).click()
        logger.info("Home button was clicked")
        print("Home button was clicked")
        # return MainPage(self.driver)

    locator_dictionary: Dict[str, Tuple[str, str]] = {
        "home_btn": (By.CLASS_NAME, "icon-home")
    }
