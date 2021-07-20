import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions

# UN: someMail@myMail.com
# Pass: MyPass321
def test_tamir():
    opts = ChromeOptions()
    # This will not close the broweser at the end of the test
    opts.add_experimental_option("detach", True)

    driver = webdriver.Chrome(executable_path="C:\\Users\\PORATY\\PycharmProjects\\TamirSelenium\\chromedriver.exe", chrome_options=opts)
    driver.get("http://automationpractice.com/index.php")
    # Wait for the site to load
    time.sleep(10)
    header = driver.find_element_by_class_name("header_user_info")
    login_btn = header.find_element_by_class_name("login")
    login_btn.click()
    # Wait for login page to load
    time.sleep(4)
    login_form = driver.find_element_by_id("login_form")
    login_form_content = login_form.find_element_by_class_name("form_content")
    email_textbox = login_form_content.find_element_by_id("email")
    email_textbox.send_keys("someMail@myMail.com")
    time.sleep(1)
    password_textbox = login_form_content.find_element_by_id("passwd")
    password_textbox.send_keys("MyPass321")
    time.sleep(1)
    submit_login_btn = login_form_content.find_element_by_id("SubmitLogin")
    submit_login_btn.click()
