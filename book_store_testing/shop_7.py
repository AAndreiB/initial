from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

driver.get('https://practice.automationtesting.in/')
driver.maximize_window()

# Shop
time.sleep(1)
myAccount = driver.find_element_by_xpath("//header[@id='header']//a[text()='Shop']")
myAccount.click()

# add a book to the cart
driver.execute_script("window.scrollBy(0, 300);")
add_button = driver.find_element_by_css_selector("a[data-product_id='165']")
add_button.click()

# open cart
time.sleep(1)
cart = driver.find_element_by_css_selector("a.wpmenucart-contents")
cart.click()

# proceed to checkout
wait = WebDriverWait(driver, 5)
proceed = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.wc-proceed-to-checkout>a.checkout-button")))
proceed.click()

# fill the gaps
first_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#billing_first_name")))
first_name.send_keys("Name")
last_name = driver.find_element_by_css_selector("input#billing_last_name")
last_name.send_keys("Last name")
email = driver.find_element_by_css_selector("input#billing_email")
email.send_keys("it.automat@yandex.ru")
phone = driver.find_element_by_css_selector("input#billing_phone")
phone.send_keys("+71234567890")
country = driver.find_element_by_css_selector("div.country_select span.select2-chosen")
country.click()
search = driver.find_element_by_css_selector("#select2-drop>.select2-search>[type='text']")
search.send_keys("Iran")

time.sleep(2)
lower = driver.find_element_by_id("select2-result-label-1104")
lower.click()

time.sleep(2)
driver.quit()

