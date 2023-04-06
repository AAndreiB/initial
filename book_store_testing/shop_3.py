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

# default sorting mode
default = driver.find_element_by_xpath("//option[text()='Default sorting']")
# check if this mode selected
assert default.get_attribute('selected')

# selector
order_by = driver.find_element_by_css_selector("select.orderby")
selector = Select(order_by)
# sorting by price
selector.select_by_visible_text('Sort by price: high to low')

time.sleep(1)
order_by = driver.find_element_by_css_selector("select.orderby")
selector = Select(order_by)

# sort mode check
default = driver.find_element_by_xpath("//option[text()='Sort by price: high to low']")
# check if this mode selected
assert default.get_attribute('selected')

time.sleep(1)
driver.quit()

