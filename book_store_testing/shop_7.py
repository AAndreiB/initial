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
search.send_keys("Russia")

selected_country = driver.find_element_by_css_selector("li.select2-result-selectable")
selected_country.click()

# address
street = driver.find_element_by_css_selector("input#billing_address_1")
street.send_keys("Lenina")
city = driver.find_element_by_css_selector("input#billing_city")
city.send_keys("Novocheboksarsk")
state = driver.find_element_by_css_selector("input#billing_state")
state.send_keys("Chuvashia")
postcode = driver.find_element_by_css_selector("input#billing_postcode")
postcode.send_keys("429900")

driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)

# payment option
payment = driver.find_element_by_css_selector("input#payment_method_cheque")
payment.click()
place_order = driver.find_element_by_css_selector("input#place_order")
place_order.click()

# check messages
wait = WebDriverWait(driver, 5)
message = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
assert message
payment_method = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//th[text()='Payment Method:']/../td"), "Check Payments"))
assert payment_method

time.sleep(1)
driver.quit()