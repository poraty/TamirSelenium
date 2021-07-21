import time

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome


def test_1():
    driver = webdriver.Chrome("/home/tamirre/PycharmProjects/pythonProject1/chromedriver")
    driver.get("http://automationpractice.com/index.php")
    header = driver.find_element_by_class_name("header_user_info")
    login_btn = header.find_element_by_class_name("login")
    login_btn.click()
    time.sleep(30)

# someMail@myMail.com
# MyPass321
def test_2():
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    # driver = Chrome(chrome_options=opts)


    driver = webdriver.Chrome(executable_path = "C:\\Users\\PORATY\\PycharmProjects\\TamirSelenium\\chromedriver.exe", chrome_options=opts)
    driver.get("https://www.youtube.com/")
    search_input = driver.find_element_by_id("search")
    time.sleep(4)
    search_input.send_keys("u2")

    search_btn = driver.find_element_by_id("search-icon-legacy")
    search_btn.click()
    driver.quit()
    # time.sleep(30)

