import infra.helper.web_element.web_element_helper as web_element_helper
from infra.helper.web_element.web_element_helper import WEB_ELEMENT_TYPE as WEB_ELEMENT_TYPE
import logic.login_page.login_page as login_page
import logic.search.search_page as search_page
import infra.helper.web_element.web_element_helper as web_element_helper

# For Shuki Site
import logging
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time
# from random import randrange
import random


# UN: someMail@myMail.com
# Pass: MyPass321
def test_tamir(init_configs, init_log, handle_web_driver):
    login_page.get_to_login_page(web_site_url=init_configs["web_site_url"], driver=handle_web_driver, logger=init_log)
    login_page.do_login(email=init_configs["email"], password=init_configs["password"], driver=handle_web_driver,
                        logger=init_log)
    login_page.click_on_home_button(driver=handle_web_driver, logger=init_log)
    product_containers_list = search_page.get_search_results(search_query="summer", driver=handle_web_driver,
                                                             logger=init_log)
    search_page.get_product_by_cost(product_containers_list, "$30.50", init_log)


def test_shuki(init_configs, handle_web_driver, init_log):
    handle_web_driver.get(init_configs["web_site_url"])
    header = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.CLASS
                                                , base_web_element=handle_web_driver
                                                , look_for="header_user_info", logger=init_log)
    init_log.info(header.text)
    print(header.text)


def test_selenium_iframe(init_configs, init_log, handle_web_driver):
    open_shuki_site(web_site_url=init_configs["Shuki_web_site_url"], driver=handle_web_driver, logger=init_log)

    # Go to page three on my website
    go_to_shuki_page("Page_three.html", handle_web_driver, init_log)

    # automation_practice_iframe = get_iframe_web_element(handle_web_driver, init_log)
    # automation_practice_iframe = handle_web_driver.find_elements_by_tag_name('iframe')[0]
    # save_the_orig_driver = handle_web_driver

    # switch to i-frame
    handle_web_driver.switch_to.frame(handle_web_driver.find_elements_by_tag_name("iframe")[0])
    # handle_web_driver = handle_web_driver.switch_to.frame(automation_practice_iframe)
    time.sleep(5)

    # Go to login page on automation practice website
    temp_get_to_login_page(driver=handle_web_driver, logger=init_log)
    # Need to add assert check to see the page is log in page.

    temp_do_login(email=init_configs["email"], password=init_configs["password"], driver=handle_web_driver,
                  logger=init_log)
    # Need to add assert check to see the log in details are as inserted.

    time.sleep(3)

    # switch back to my html driver
    handle_web_driver.switch_to.parent_frame()

    # Go to page one on my website
    go_to_shuki_page("Page_one.html", handle_web_driver, init_log)
    # Need to add assert check to see the page is one.


def test_button_accept(init_configs, init_log, handle_web_driver):
    open_shuki_site(web_site_url=init_configs["Shuki_web_site_url"], driver=handle_web_driver, logger=init_log)
    click_on_background_page_one_button(handle_web_driver, init_log)
    alert_driver: webdriver = handle_web_driver.switch_to.alert
    alert_message = alert_driver.text
    init_log.info(f"The alert message is: {alert_message}")
    print(f"\nThe alert message is: {alert_message}")
    alert_driver.accept()
    time.sleep(5)
    maccabi_logo_list = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.ID_LIST
                                              , base_web_element=handle_web_driver
                                              , look_for="maccabi_logo"
                                              , logger=init_log)
    init_log.info(f"maccabi_logo_list size={len(maccabi_logo_list)}")
    print(f"maccabi_logo_list size={len(maccabi_logo_list)}")
    assert len(maccabi_logo_list) == 1, f"There is not exactly one logo. expected=1 actual={len(maccabi_logo_list)}"


def test_button_dismiss(init_configs, init_log, handle_web_driver):
    open_shuki_site(web_site_url=init_configs["Shuki_web_site_url"], driver=handle_web_driver, logger=init_log)
    click_on_background_page_one_button(handle_web_driver, init_log)
    alert_driver: webdriver = handle_web_driver.switch_to.alert
    alert_message = alert_driver.text
    init_log.info(f"The alert message is: {alert_message}")
    print(f"\nThe alert message is: {alert_message}")
    time.sleep(2)
    alert_driver.dismiss()
    time.sleep(7)
    maccabi_logo_list = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.ID_LIST
                                              , base_web_element=handle_web_driver
                                              , look_for="maccabi_logo"
                                              , logger=init_log)
    init_log.info(f"maccabi_logo_list size={len(maccabi_logo_list)}")
    print(f"maccabi_logo_list size={len(maccabi_logo_list)}")
    assert len(maccabi_logo_list) == 0, f"There is at least one logo. expected=1 actual={len(maccabi_logo_list)}"


def test_dropdown_selection_random(init_configs, init_log, handle_web_driver):
    selection_options = ["Maccabi", "Google", "Automation_Practice"]
    # index = randrange(3)
    index = random.randint(0, 2)
    selection = selection_options[index]
    init_log.info(f"The selected option is: {selection}")
    print(f"\nThe selected option is: {selection}")
    open_shuki_site(web_site_url=init_configs["Shuki_web_site_url"], driver=handle_web_driver, logger=init_log)
    dropdown = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.ID
                                              , base_web_element=handle_web_driver
                                              , look_for="dropdown"
                                              , logger=init_log)
    dropdown.click()

    # To show the click
    time.sleep(2)

    option_selection = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.ID
                                              , base_web_element=handle_web_driver
                                              , look_for=selection
                                              , logger=init_log)
    option_selection.click()

    # To show the click
    time.sleep(2)
    dropdown.click()

    automation_practice = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.ID
                                              , base_web_element=handle_web_driver
                                              , look_for="automationpractice_photo"
                                              , logger=init_log)
    automation_practice_selection = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.ID_LIST
                                              , base_web_element=automation_practice
                                              , look_for=selection
                                              , logger=init_log)
    init_log.info(f"automation_practice_selection size={len(automation_practice_selection)}")
    print(f"automation_practice_selection size={len(automation_practice_selection)}")
    assert len(automation_practice_selection) == 1, f"There is not exactly one logo for {selection}. expected=1 actual={len(automation_practice_selection)}"

    background_id = automation_practice_selection[0].get_attribute("id")
    init_log.info(f"automation_practice_selection id={background_id}")
    print(f"automation_practice_selection id={background_id}")
    assert background_id == selection, f"The id of the background is not {selection}. but is= {background_id}"


# Functions just for this test
def open_shuki_site(web_site_url: str, driver: webdriver, logger: logging.Logger):
    logger.info(f"Opening the address: {web_site_url}")
    driver.get(web_site_url)


def go_to_shuki_page(href: str, base_web_element: WebElement, logger: logging.Logger):
    navbar = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.CLASS
                                                , base_web_element=base_web_element
                                                , look_for="navbar"
                                                , logger=logger)

    page = navbar.find_element_by_xpath('//a[@href="' + href + '"]')
    page.click()


def get_iframe_web_element(driver: webdriver, logger: logging.Logger):
    return web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.ID
                                              , base_web_element=driver
                                              , look_for="automation_practice_iframe"
                                              , logger=logger)


def temp_get_to_login_page(driver: webdriver, logger: logging.Logger):
    # driver.get(web_site_url)
    header = driver.find_element_by_class_name("header_user_info")
    login_btn = header.find_element_by_class_name("login")
    login_btn.click()
    logger.info("After clicking on login button")


def temp_do_login(email, password, driver, logger: logging.Logger):
    login_form = driver.find_element_by_id("login_form")
    login_form_content = login_form.find_element_by_class_name("form_content")
    # Enter mail
    login_form_content.find_element_by_id("email").send_keys(email)
    # Enter password
    login_form_content.find_element_by_id("passwd").send_keys(password)
    # Click on submit
    login_form_content.find_element_by_id("SubmitLogin").click()
    logger.info("Submit login button was clicked")
    print("Submit login button was clicked")


def click_on_background_page_one_button(driver: webdriver, logger: logging.Logger):
    button = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.ID
                                              , base_web_element=driver
                                              , look_for="alert_button"
                                              , logger=logger)
    logger.info("About to click on the background page one button")
    button.click()
    logger.info("The background page one button was clicked")

