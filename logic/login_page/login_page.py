import time
from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.remote.webelement import WebElement
import infra.helper.web_element.web_element_helper as web_element_helper
from infra.helper.web_element.web_element_helper import WEB_ELEMENT_TYPE as WEB_ELEMENT_TYPE
import logging


def get_to_login_page(web_site_url: str, driver: webdriver, logger: logging.Logger):
    driver.get(web_site_url)
    header = driver.find_element_by_class_name("header_user_info")
    login_btn = header.find_element_by_class_name("login")
    login_btn.click()
    logger.info("After clicking on login button")
    # Wait for login page to load
    # time.sleep(4)


def do_login(email, password, driver, logger: logging.Logger) -> WebElement:
    login_form = driver.find_element_by_id("login_form")
    login_form_content = login_form.find_element_by_class_name("form_content")
    # Enter mail
    login_form_content.find_element_by_id("email").send_keys(email)
    # Enter password
    login_form_content.find_element_by_id("passwd").send_keys(password)
    # Click on submit
    login_form_content.find_element_by_id("SubmitLogin").click()
    logger.info("Submit login button was clicked")
    class_name = "myaccount-link-list"
    return web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.CLASS
                                              , base_web_element=driver
                                              , look_for=class_name
                                              , logger=logger)
    # return web_element_helper.get_class_web_element(class_name, driver=driver)


def click_on_home_button(driver: webdriver, logger: logging.Logger):
    web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.CLASS
                                       , base_web_element=driver
                                       , look_for="icon-home"
                                       , logger=logger).click()
    web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.ID
                                       , base_web_element=driver
                                       , look_for="home-page-tabs"
                                       , logger=logger)
