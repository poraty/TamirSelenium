from selenium import webdriver
from logic.page.basic_page import BasicPage
import logging
from logic.page.login_page import LoginPage
from typing import Dict, Tuple
from selenium.webdriver.common.by import By
import time
from logic.page.search_result_page import SearchResultPage


class MainPage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def get_to_login_page(self, logger: logging.Logger) -> LoginPage:
        self.find_element_and_color_it(*self.locator_dictionary['login_btn']).click()
        logger.info("After clicking on login button")
        return LoginPage(self.driver)

    def search(self, search_query: str, logger: logging.Logger) -> SearchResultPage:
        logger.info(f"About to search for= {search_query}")
        print(f"About to search for= {search_query}")
        # Write the search query
        self.find_element_and_color_it(*self.locator_dictionary['search_textbox']).send_keys(search_query)

        # Click on search button
        self.find_element_and_color_it(*self.locator_dictionary['search_btn']).click()
        time.sleep(4)
        return SearchResultPage(self.driver)

    locator_dictionary: Dict[str, Tuple[str, str]] = {
        "login_btn": (By.CLASS_NAME, "login"),
        "home-page-tabs": (By.CLASS_NAME, "home-page-tabs"),
        "search_textbox": (By.CLASS_NAME, "search_query"),
        "search_btn": (By.CLASS_NAME, "button-search")
    }
