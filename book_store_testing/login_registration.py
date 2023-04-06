from selenium import webdriver
import time

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

driver.get('https://practice.automationtesting.in/')
driver.maximize_window()

# My Account menu
myAccount = driver.find_element_by_xpath('//a[text()="My Account"]') # using different types of selectors
myAccount.click()

# register user
email = driver.find_element_by_css_selector("form.register input[type='email']")
email.send_keys('qa.automat@yandex.ru')
password = driver.find_element_by_css_selector("form.register input[type='password']")
password.send_keys('secret_code')
submit = driver.find_element_by_css_selector("form.register input[type='submit']")
submit.click()

time.sleep(3)
driver.quit()
