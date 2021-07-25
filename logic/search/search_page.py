from selenium import webdriver
import infra.helper.web_element.web_element_helper as web_element_helper
from infra.helper.web_element.web_element_helper import WEB_ELEMENT_TYPE as WEB_ELEMENT_TYPE
import time
from selenium.webdriver.remote.webelement import WebElement
import logging


def get_search_results(search_query: str, driver: webdriver, logger: logging.Logger) -> list:
    search_block_top = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.ID
                                                          , base_web_element=driver
                                                          , look_for="search_block_top"
                                                          , logger=logger)

    # Write the search query
    web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.CLASS
                                       , base_web_element=search_block_top
                                       , look_for="search_query", logger=logger).send_keys(search_query)

    # Click on search button
    web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.CLASS
                                       , base_web_element=search_block_top
                                       , look_for="button-search", logger=logger).click()

    time.sleep(4)
    # base_product_list = get_class_web_element("product_list", driver=driver)
    base_product_list = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.CLASS
                                                           , base_web_element=driver
                                                           , look_for="product_list", logger=logger)

    # product_containers_list = get_class_web_elements(base_product_list, "product-container")
    product_containers_list = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.CLASSES_LIST
                                                                 , base_web_element=base_product_list
                                                                 , look_for="product-container", logger=logger)

    logger.info(type(product_containers_list))
    logger.info(len(product_containers_list))
    # print(type(product_containers_list))
    # print(len(product_containers_list))
    assert 0 < len(product_containers_list), f"No items were found for the search query= {search_query}"
    return product_containers_list


def get_product_by_cost(product_containers_list: list, cost: str, logger: logging.Logger) -> WebElement:
    for elm in product_containers_list:
        logger.info(elm.find_element_by_class_name("right-block").find_element_by_class_name("price").text)
        # print(elm.find_element_by_class_name("right-block").find_element_by_class_name("price").text)
        # Why this is not the right action to get the cost?
        # print(elm.find_element_by_class_name("product-price").text)

        # The right action
        is_found = (cost == elm.find_element_by_class_name("right-block").find_element_by_class_name("price").text)
        logger.info(is_found)
        # print(is_found)
        if is_found:
            # elm.click()
            logger.info(f"The item with the cost= {cost} is found!")
            # print(f"The item with the cost= {cost} is found!")
            return elm

    assert False, f"Didn't find the cost: {cost}"
