import time
from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.remote.webelement import WebElement

driver = None


def get_driver() -> webdriver:
    opts = ChromeOptions()
    # This will not close the broweser at the end of the test
    opts.add_experimental_option("detach", True)

    return webdriver.Chrome(executable_path="C:\\Users\\PORATY\\PycharmProjects\\TamirSelenium\\chromedriver.exe", chrome_options=opts)


def test_something():
    global driver
    driver = get_driver()
    get_to_login_page()
    class_name = "myaccount-link-list"
    get_class_web_element(class_name)


# def do_login(email, password):
#     login_form = driver.find_element_by_id("login_form")
#     login_form_content = login_form.find_element_by_class_name("form_content")
#     # Enter mail
#     login_form_content.find_element_by_id("email").send_keys(email)
#     # Enter password
#     login_form_content.find_element_by_id("passwd").send_keys(password)
#     # Click on submit
#     login_form_content.find_element_by_id("SubmitLogin").click()


# UN: someMail@myMail.com
# Pass: MyPass321
def test_tamir():
    global driver
    driver = get_driver()
    get_to_login_page()
    do_login(email="someMail@myMail.com", password="MyPass321")
    click_on_home_button()
    product_containers_list = get_search_results("summer")
    # get_product_by_sum(product_containers_list, "30.50")
    get_product_by_cost(product_containers_list, "\n$30.50\n")


def get_to_login_page():
    driver.get("http://automationpractice.com/index.php")
    header = driver.find_element_by_class_name("header_user_info")
    login_btn = header.find_element_by_class_name("login")
    login_btn.click()
    # Wait for login page to load
    time.sleep(4)


def do_login(email, password):
    login_form = driver.find_element_by_id("login_form")
    login_form_content = login_form.find_element_by_class_name("form_content")
    # Enter mail
    login_form_content.find_element_by_id("email").send_keys(email)
    # Enter password
    login_form_content.find_element_by_id("passwd").send_keys(password)
    # Click on submit
    login_form_content.find_element_by_id("SubmitLogin").click()
    class_name = "myaccount-link-list"
    get_class_web_element(class_name)


def get_class_web_element(class_name: str) -> WebElement:
    try:
        return driver.find_element_by_class_name(class_name)
    except NoSuchElementException as e:
        assert False, f"Failed to find the class name: {class_name}. error={str(e)}"


def get_class_web_element_with_base(current_base_class: WebElement, class_name: str) -> WebElement:
    try:
        return current_base_class.find_element_by_class_name(class_name)
    except NoSuchElementException as e:
        assert False, f"Failed to find the class name: {class_name}. error={str(e)}"


def get_class_web_elements(current_base_class: WebElement, class_name: str) -> list:
    try:
        return current_base_class.find_elements_by_class_name(class_name)
    except NoSuchElementException as e:
        assert False, f"Failed to find the class name: {class_name}. error={str(e)}"


def get_id_web_element(id: str) -> WebElement:
    try:
        return driver.find_element_by_id(id)
    except NoSuchElementException as e:
        assert False, f"Failed to find the id: {id}. error={str(e)}"


def get_id_web_element_by_base(current_base_element: WebElement, id: str) -> WebElement:
    try:
        return current_base_element.find_element_by_id(id)
    except NoSuchElementException as e:
        assert False, f"Failed to find the id: {id}. error={str(e)}"


def click_on_home_button():
    get_class_web_element("icon-home").click()
    get_id_web_element("home-page-tabs")


def get_search_results(search_query: str) -> list:
    search_block_top = get_id_web_element("search_block_top")

    # Write the search query
    get_class_web_element_with_base(search_block_top, "search_query").send_keys(search_query)

    # Click on search button
    get_class_web_element_with_base(search_block_top, "button-search").click()
    time.sleep(4)
    base_product_list = get_class_web_element("product_list")
    product_containers_list = get_class_web_elements(base_product_list, "product-container")
    print(type(product_containers_list))
    print(len(product_containers_list))
    assert 0 < len(product_containers_list), f"No items were found for the search query= {search_query}"
    return product_containers_list


def get_product_by_cost(product_containers_list: list, cost: str) -> WebElement:
    for elm in product_containers_list:

        # Why this is not the right action to get the cost?
        # print(elm.find_element_by_class_name("product-price").text)

        # The right action
        is_found = cost in elm.text
        print(is_found)
        if is_found:
            # elm.click()
            print(f"The item with the cost= {cost} is found! it's text= {elm.text}")
            return elm

    assert False, f"Didn't find the cost: {cost}"


