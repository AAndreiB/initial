from selenium import webdriver
import time

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

driver.get('https://practice.automationtesting.in/')
driver.maximize_window()

# My Account menu
myAccount = driver.find_element_by_xpath('//a[text()="My Account"]') # using different types of selectors
myAccount.click()

# register user
time.sleep(1)
email = driver.find_element_by_css_selector("form.register input[type='email']")
email.send_keys('it.automat@yandex.ru')
time.sleep(1)
password = driver.find_element_by_css_selector("form.register input[type='password']")
password.send_keys('secret_code_1234')
time.sleep(1)
register = driver.find_element_by_css_selector("input[name='register']")
register.click()

time.sleep(5)
driver.quit()

