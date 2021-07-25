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


def test_selenium(init_configs, init_log, handle_web_driver):
    open_shuki_site(web_site_url=init_configs["Shuki_web_site_url"], driver=handle_web_driver, logger=init_log)
    go_to_page_three("Page_three.html", handle_web_driver, init_log)

    # automation_practice_iframe = get_iframe_web_element(handle_web_driver, init_log)
    # automation_practice_iframe = handle_web_driver.find_elements_by_tag_name('iframe')[0]
    save_the_orig_driver = handle_web_driver
    handle_web_driver.switch_to.frame(handle_web_driver.find_elements_by_tag_name("iframe")[0])
    # handle_web_driver = handle_web_driver.switch_to.frame(automation_practice_iframe)
    time.sleep(5)
    temp_get_to_login_page(driver=handle_web_driver, logger=init_log)
    login_page.do_login(email=init_configs["email"], password=init_configs["password"], driver=handle_web_driver,
                        logger=init_log)
    login_page.click_on_home_button(driver=handle_web_driver, logger=init_log)


# Functions just for this test
def open_shuki_site(web_site_url: str, driver: webdriver, logger: logging.Logger):
    logger.info(f"Opening the address: {web_site_url}")
    driver.get(web_site_url)


def go_to_page_three(href: str, base_web_element: WebElement, logger: logging.Logger):
    navbar = web_element_helper.get_web_element(web_element_type=WEB_ELEMENT_TYPE.CLASS
                                       , base_web_element=base_web_element
                                       , look_for="navbar"
                                       , logger=logger)

    page_two = navbar.find_element_by_xpath('//a[@href="'+href+'"]')
    page_two.click()


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
