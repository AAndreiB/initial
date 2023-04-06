from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

driver.get('https://practice.automationtesting.in/')
driver.maximize_window()

# My Account menu
myAccount = driver.find_element_by_xpath('//a[text()="My Account"]') # using different types of selectors
myAccount.click()

# login
time.sleep(1)
email = driver.find_element_by_css_selector("form.login input[type='text']")
email.send_keys('it.automat@yandex.ru')
time.sleep(1)
password = driver.find_element_by_css_selector("form.login input[type='password']")
password.send_keys('secret_code_1234')
time.sleep(1)
submit = driver.find_element_by_css_selector("form.login input[type='submit']")
submit.click()

# Shop
time.sleep(1)
myAccount = driver.find_element_by_xpath("//header[@id='header']//a[text()='Shop']")
myAccount.click()

# add to cart
driver.execute_script("window.scrollBy(0, 500);")
add_button = driver.find_element_by_css_selector("a[data-product_id='165']")
add_button.click()
time.sleep(1)
add_button = driver.find_element_by_css_selector("a[data-product_id='165']")
add_button.click()

# open cart
cart = driver.find_element_by_css_selector("a.wpmenucart-contents")
cart.click()

time.sleep(3)
driver.quit()

