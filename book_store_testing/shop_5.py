from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
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
time.sleep(1)
add_button = driver.find_element_by_css_selector("a[data-product_id='165']")
add_button.click()

# check amount
time.sleep(1)
items = driver.find_element_by_css_selector("a.wpmenucart-contents>span.cartcontents")
assert items.text == '1 Item'
amount = driver.find_element_by_css_selector("a.wpmenucart-contents>span.amount")
assert amount.text == "₹350.00"

# open cart
cart = driver.find_element_by_css_selector("a.wpmenucart-contents")
cart.click()

wait = WebDriverWait(driver, 5)
# subtotal = driver.find_element_by_css_selector("td[data-title='Subtotal']")
subtotal = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "td[data-title='Subtotal']")))
assert subtotal.text == "₹350.00" # check the value

# total = driver.find_element_by_css_selector("td[data-title='Total']")
total = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "td[data-title='Total']")))
assert total.text is not None # check that is not empty field

time.sleep(3)
driver.quit()

