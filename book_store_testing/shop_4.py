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

# find book
book = driver.find_element_by_css_selector("img[title='Android Quick Start Guide']")
book.click()

del_price = driver.find_element_by_css_selector("div.summary p.price>del>span")
assert del_price.text == "₹600.00"
new_price = driver.find_element_by_css_selector("div.summary p.price>ins>span")
assert new_price.text == "₹450.00"

driver.implicitly_wait(3)
image = driver.find_element_by_css_selector("img[title='Android Quick Start Guide']")
image.click()

time.sleep(5)
close = driver.find_element_by_css_selector("a.pp_close")
close.click()

time.sleep(1)
driver.quit()

