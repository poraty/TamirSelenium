import time
from typing import List

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from definitions import SHUKI_HTML_PAGE_ONE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_actions(init_configs, init_log, handle_web_driver):
    web_site_url = "http://demo.guru99.com/test/drag_drop.html"
    init_log.info(f"Opening the address: {web_site_url}")
    handle_web_driver.get(web_site_url)
    num5000_list: List[WebElement] = handle_web_driver.find_elements_by_css_selector("#fourth > a")
    print(num5000_list)
    smallest_x_index = 0
    smallest_x = -1
    index = 0
    for elm in num5000_list:
        pass
        if smallest_x == -1:
            smallest_x = elm.location['x']
            index = +1
            break

        if elm.location['x'] < smallest_x:
            smallest_x = elm.location['x']
            smallest_x_index = index

        index = +1

    left5000 = num5000_list.pop(smallest_x_index)
    # print(f"\nleft5000.x={left5000.location['x']} left5000.y={left5000.location['y']}")
    debit_amount_place_holder = handle_web_driver.find_element_by_css_selector("#amt7 > li.placeholder")
    # print(f"debit_amount_place_holder.x={debit_amount_place_holder.location['x']} debit_amount_place_holder.y={debit_amount_place_holder.location['y']}")

    right5000 = num5000_list[0]
    # print(f"\nright5000.x={right5000.location['x']} right5000.y={right5000.location['y']}")
    credit_amount_place_holder = handle_web_driver.find_element_by_css_selector("#amt8 > li.placeholder")
    # print(f"credit_amount_place_holder.x={credit_amount_place_holder.location['x']} credit_amount_place_holder.y={credit_amount_place_holder.location['y']}")

    bank = handle_web_driver.find_element_by_css_selector("#credit2 > a")
    debit_account_place_holder = handle_web_driver.find_element_by_css_selector("#bank > li.placeholder")

    sales = handle_web_driver.find_element_by_css_selector("#credit1 > a")
    credit_account_place_holder = handle_web_driver.find_element_by_css_selector("#loan > li.placeholder")

    # create action chain object
    action = ActionChains(handle_web_driver)

    pause_for = 1

    # drag and drop the item
    action.drag_and_drop(left5000, debit_amount_place_holder)
    action.pause(pause_for)
    action.drag_and_drop(right5000, credit_amount_place_holder)
    action.pause(pause_for)
    action.drag_and_drop(bank, debit_account_place_holder)
    action.pause(pause_for)
    action.drag_and_drop(sales, credit_account_place_holder)

    # perform the operation
    action.perform()

    result = handle_web_driver.find_element_by_css_selector("#equal.table4_result > a").text

    assert result == "Perfect!", f"actual= {result}"
    time.sleep(3)


def test_wait(init_configs, init_log, handle_web_driver):
    init_log.info(f"Opening the address: {SHUKI_HTML_PAGE_ONE}")
    handle_web_driver.get(SHUKI_HTML_PAGE_ONE)
    handle_web_driver.find_element_by_css_selector("#alert_button").click()
    time.sleep(3)
    alert_driver: webdriver = handle_web_driver.switch_to.alert
    alert_message = alert_driver.text
    init_log.info(f"The alert message is: {alert_message}")
    print(f"\nThe alert message is: {alert_message}")
    alert_driver.accept()
    maccabi_logo = wait_until_element_is_located(driver=handle_web_driver, css="#maccabi_logo", time_to_wait=5)
    assert maccabi_logo.text == "maccabi_logo"


def test_wait_less_time(init_configs, init_log, handle_web_driver):
    init_log.info(f"Opening the address: {SHUKI_HTML_PAGE_ONE}")
    handle_web_driver.get(SHUKI_HTML_PAGE_ONE)
    handle_web_driver.find_element_by_css_selector("#alert_button").click()
    time.sleep(1)
    alert_driver: webdriver = handle_web_driver.switch_to.alert
    alert_message = alert_driver.text
    init_log.info(f"The alert message is: {alert_message}")
    print(f"\nThe alert message is: {alert_message}")
    alert_driver.accept()
    try:
        wait_until_element_is_located(driver=handle_web_driver, css="#maccabi_logo", time_to_wait=1)
        assert False, "The timeout was not long enough!"
    except TimeoutException as e:
        # assert e.__class__ == TimeoutException.__class__, f"The exception was not TimeoutException but was {e.msg}"
        print("The exception was TimeoutException")
        assert True


def wait_until_element_is_located(driver: webdriver, css: str, time_to_wait: int) -> WebElement:
    return WebDriverWait(driver, time_to_wait).until(ec.visibility_of_element_located((By.CSS_SELECTOR, css)))
