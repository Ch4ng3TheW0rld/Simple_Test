from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from time import sleep


# Type Amazon credentials
username = input("Enter the username: ")
password = getpass("Enter the password: ")
url = "https://www.amazon.com/"


# For this example Firefox browser was used (for Chrome change the driver)
driver = webdriver.Firefox()
driver.get(url)
driver.set_page_load_timeout(12)  # adjust the time if internet speed is slow

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

# Use search bar to search product
sleep(3)
searchbar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbar.send_keys('alienware')
searchbar.send_keys(Keys.ENTER)

# select the first product
sleep(3)
item = driver.find_element_by_css_selector('span.a-size-medium').click()

# add to cart
sleep(3)
addtocart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
addtocart.click()

# proceed to purchase
sleep(3)
proceed = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/span/span/input')
proceed.click()

