import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from logic.page.login_page import LoginPage
from logic.page.main_page import MainPage
from selenium.webdriver.remote.webelement import WebElement
from typing import List
import logic.search.search_page as search_page_helper


class TestPageObject(object):
# mainPage.clickSignIn => signInPage
# signInPage.login("user","password") => MyAccountPage
# MyAccountPage.clickHome => mainPage
# mainPage.search("summer")=>searchResultPage

    def test_page_object(self, init_configs, init_log, setup_main_page):
        login_page: LoginPage = setup_main_page.get_to_login_page(logger=init_log)
        my_account_page = login_page.do_login(email=init_configs["email"], password=init_configs["password"], logger=init_log)
        # setup_main_page = my_account_page.click_on_home_button(logger=init_log)
        my_account_page.click_on_home_button(logger=init_log)
        search_result_page = setup_main_page.search(search_query="summer", logger=init_log)
        product_containers_list: List[WebElement] = search_result_page.get_search_results(logger=init_log)
        item: WebElement = search_page_helper.get_product_by_cost(product_containers_list, "$30.50", init_log)
        item.click()
        time.sleep(5)
        # signInPage : SignInPage = setup_main_page.clickSighnIn()
        # myAccountPage : MyAccountPage = signInPage.login("user", "password")
        # mainPage : MainPage = myAccountPage.clickHome()
        # searchResultPage :SearchResultPage=mainPage.search("summer")
