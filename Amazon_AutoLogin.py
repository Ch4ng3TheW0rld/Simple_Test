from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
from time import sleep

# Type Amazon credentials
username = input("Enter the username: ")
password = getpass("Enter the password: ")
url = "https://www.amazon.com/"


# For this example Firefox browser was used (for Chrome change the driver)
driver = webdriver.Firefox()
driver.get(url)
driver.set_page_load_timeout(10)  # adjust the time if internet speed is slow

# find SignIn in nav bar
SignIn_button = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
SignIn_button.click()

# Auto-Fill the username then continue
sleep(3)  # adjust the time if internet speed is slow
username_textbox = driver.find_element_by_id("ap_email")
username_textbox.send_keys(username)
Continue_button = driver.find_element_by_id("continue")
Continue_button.submit()

# Auto-Fill the password to complete the Login process
sleep(3) # adjust the time if internet speed is slow
password_textbox = driver.find_element_by_id("ap_password")
password_textbox.send_keys(password)
SignIn_button = driver.find_element_by_id("auth-signin-button-announce")
SignIn_button.submit()