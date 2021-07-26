from enum import Enum
from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
import logging

class WEB_ELEMENT_TYPE(Enum):
    CLASS = "class",
    ID = "id",
    CLASSES_LIST = "classes_list",
    ID_LIST = "id_list"


def find_class(current_base: WebElement, look_for: str, logger: logging.Logger): return get_class_web_element_with_base(current_base_class=current_base
                                                                                                                        , class_name=look_for
                                                                                                                        , logger=logger)


def find_classes_list(current_base: WebElement, look_for: str, logger: logging.Logger): return get_class_web_elements(current_base_class=current_base
                                                                                                                      , class_name=look_for
                                                                                                                      , logger=logger)


def find_id(current_base: WebElement, look_for: str, logger: logging.Logger): return get_id_web_element_by_base(current_base_element=current_base
                                                                                                                , look_for_id=look_for
                                                                                                                , logger=logger)


def find_id_list(current_base: WebElement, look_for: str, logger: logging.Logger): return get_id_web_elements(current_base_element=current_base
                                                                                                                , look_for_id=look_for
                                                                                                                , logger=logger)


find_functions = {
                    WEB_ELEMENT_TYPE.CLASS.value: find_class,
                    WEB_ELEMENT_TYPE.CLASSES_LIST.value: find_classes_list,
                    WEB_ELEMENT_TYPE.ID.value: find_id,
                    WEB_ELEMENT_TYPE.ID_LIST.value: find_id_list
                  }


def get_web_element(web_element_type: WEB_ELEMENT_TYPE, base_web_element: WebElement, look_for: str, logger: logging.Logger):
    return find_functions[web_element_type.value](current_base=base_web_element, look_for=look_for, logger=logger)

    # if web_element_type.value == WebElementType.CLASS:
    #     return find_functions[WebElementType.CLASS](current_base_class=base_web_element, class_name=look_for)
    #     # return get_class_web_element_with_base(current_base_class=base_web_element, class_name=look_for)
    #
    # if web_element_type.value == WebElementType.CLASSES_LIST:
    #     return get_class_web_elements(current_base_class=base_web_element, class_name=look_for)
    #
    # if web_element_type.value == WebElementType.ID:
    #     return get_id_web_element_by_base(current_base_element=base_web_element, look_for_id=look_for)


def get_class_web_element(current_base: WebElement, look_for: str, logger: logging.Logger) -> WebElement:
    try:
        logger.info(f"Getting the web element by class name: {look_for}")
        return current_base.find_element_by_class_name(look_for)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the class name: {class_name}. error={str(e)}"
        logger.error(f"Failed to find the class name: {look_for}. error={str(e)}")
        print(f"Failed to find the class name: {look_for}. error={str(e)}")  # Will add the log later
        raise e


def get_class_web_element_with_base(current_base_class: WebElement, class_name: str, logger: logging.Logger) -> WebElement:
    try:
        logger.info(f"Getting the web element by class name: {class_name}")
        return current_base_class.find_element_by_class_name(class_name)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the class name: {class_name}. error={str(e)}"
        logger.error(f"Failed to find the class name: {class_name}. error={str(e)}")
        print(f"Failed to find the class name: {class_name}. error={str(e)}")  # Will add the log later
        raise e


def get_class_web_elements(current_base_class: WebElement, class_name: str, logger: logging.Logger) -> List[WebElement]:
    try:
        logger.info(f"Getting the web elements list by class name: {class_name}")
        return current_base_class.find_elements_by_class_name(class_name)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the class name: {class_name}. error={str(e)}"
        logger.error(f"Failed to find the class name: {class_name}. error={str(e)}")
        print(f"Failed to find the class name: {class_name}. error={str(e)}")  # Will add the log later
        raise e


def get_id_web_element(id: str, driver: webdriver, logger: logging.Logger) -> WebElement:
    try:
        logger.info(f"Getting the web element by id: {id}")
        return driver.find_element_by_id(id)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the id: {id}. error={str(e)}"
        logger.error(f"Failed to find the id: {id}. error={str(e)}")
        print(f"Failed to find the id: {id}. error={str(e)}")  # Will add the log later
        raise e


def get_id_web_element_by_base(current_base_element: WebElement, look_for_id: str, logger: logging.Logger) -> WebElement:
    try:
        logger.info(f"Getting the web element by id: {look_for_id}")
        return current_base_element.find_element_by_id(look_for_id)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the id: {id}. error={str(e)}"
        logger.error(f"Failed to find the id: {id}. error={str(e)}")
        print(f"Failed to find the id: {id}. error={str(e)}")  # Will add the log later
        raise e


def get_id_web_elements(current_base_element: WebElement, look_for_id: str, logger: logging.Logger) -> List[WebElement]:
    try:
        logger.info(f"Getting the web elements list by the id: {look_for_id}")
        return current_base_element.find_elements_by_id(look_for_id)
    except NoSuchElementException as e:
        # assert False, f"Failed to find the class name: {class_name}. error={str(e)}"
        logger.error(f"Failed to find the id: {look_for_id}. error={str(e)}")
        print(f"Failed to find the id: {look_for_id}. error={str(e)}")  # Will add the log later
        raise e
