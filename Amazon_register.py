from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
from time import sleep
from selenium.webdriver.common.by import By

# Data to Sign-Up
name = input("Enter in your name: ")
username = input("Enter in your username: ")
password = getpass("Enter in your password: ")
url = "https://www.amazon.com/"

# For this example Firefox browser was used (for Chrome change the driver)
driver = webdriver.Firefox()
action = ActionChains(driver)
driver.get(url)
driver.set_page_load_timeout(10)  # adjust the time if internet speed is slow

# find SignUp in nav bar
sleep(3)   # adjust the time if internet speed is slow
Account_list = driver.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
action.move_to_element(Account_list).perform()
sleep(3)
SignUp_button = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[3]/div[2]/div[2]/div/div[1]/div/div/a').click()

# Auto-Fill user information to register
sleep(3)   # adjust the time if internet speed is slow
name_textbox = driver.find_element_by_id("ap_customer_name")
name_textbox.send_keys(name)
username_textbox = driver.find_element_by_id("ap_email")
username_textbox.send_keys(username)
password_textbox = driver.find_element_by_id("ap_password")
password_textbox.send_keys(password)
password2_textbox = driver.find_element_by_id("ap_password_check")
password2_textbox.send_keys(password)
Continue_button = driver.find_element_by_id("continue")
Continue_button.submit()
