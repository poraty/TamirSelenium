import logging
import time
from selenium import webdriver
from logic.page.basic_page import BasicPage
from typing import Dict, Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SearchResultPage(BasicPage):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def get_search_results(self, logger: logging.Logger) -> List[WebElement]:
        product_containers_list: List[WebElement] = self.find_multi_elements_and_color_them(*self.locator_dictionary['search_results'])
        logger.info(type(product_containers_list))
        logger.info(len(product_containers_list))
        # print(type(product_containers_list))
        # print(len(product_containers_list))
        assert 0 < len(product_containers_list), f"No items were found for the search query"
        return product_containers_list


    locator_dictionary: Dict[str, Tuple[str, str]] = {
        "search_textbox": (By.CLASS_NAME, "search_query"),
        "search_results": (By.CLASS_NAME, "product-container")
    }


