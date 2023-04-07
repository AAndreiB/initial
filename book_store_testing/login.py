from selenium import webdriver
import time

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

driver.get('https://practice.automationtesting.in/')
driver.maximize_window()

# My Account menu
myAccount = driver.find_element_by_xpath('//a[text()="My Account"]') # using different types of selectors
myAccount.click()

time.sleep(1)
email = driver.find_element_by_css_selector("form.login input[type='text']")
email.send_keys('it.automat@yandex.ru')
time.sleep(1)
password = driver.find_element_by_css_selector("form.login input[type='password']")
password.send_keys('secret_code_1234')
time.sleep(1)
submit = driver.find_element_by_css_selector("form.login input[type='submit']")
submit.click()

time.sleep(5)
driver.quit()

