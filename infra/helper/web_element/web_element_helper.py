from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


def get_class_web_element(class_name: str, driver: webdriver) -> WebElement:
    try:
        return driver.find_element_by_class_name(class_name)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the class name: {class_name}. error={str(e)}"
        print(f"Failed to find the class name: {class_name}. error={str(e)}")  # Will add the log later
        raise e


def get_class_web_element_with_base(current_base_class: WebElement, class_name: str) -> WebElement:
    try:
        return current_base_class.find_element_by_class_name(class_name)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the class name: {class_name}. error={str(e)}"
        print(f"Failed to find the class name: {class_name}. error={str(e)}")  # Will add the log later
        raise e


def get_class_web_elements(current_base_class: WebElement, class_name: str) -> List[WebElement]:
    try:
        return current_base_class.find_elements_by_class_name(class_name)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the class name: {class_name}. error={str(e)}"
        print(f"Failed to find the class name: {class_name}. error={str(e)}")  # Will add the log later
        raise e


def get_id_web_element(id: str, driver: webdriver) -> WebElement:
    try:
        return driver.find_element_by_id(id)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the id: {id}. error={str(e)}"
        print(f"Failed to find the id: {id}. error={str(e)}")  # Will add the log later
        raise e


def get_id_web_element_by_base(current_base_element: WebElement, id: str) -> WebElement:
    try:
        return current_base_element.find_element_by_id(id)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the id: {id}. error={str(e)}"
        print(f"Failed to find the id: {id}. error={str(e)}")  # Will add the log later
        raise e
