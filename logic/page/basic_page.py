from typing import Dict, Tuple
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class BasicPage(object):
    def __init__(self, driver: webdriver):
        self.driver = driver

    def find_element_and_color_it(self, by_find: str, token: str, wait=10) -> WebElement:
        if wait > 0:
            element = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((by_find, token)))
            self.driver.execute_script("arguments[0].setAttribute('style', 'color:red;')", element)
        else:
            element = self.driver.find_element(by_find, token)
        return element

    def find_multi_elements_and_color_them(self, by_find, token) -> List[WebElement]:
        elements = WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located((by_find, token)))
        for element in elements:
            self.driver.execute_script("arguments[0].setAttribute('style', 'color:red;')", element)
        return elements


