from selenium import webdriver
import time

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

driver.get('https://practice.automationtesting.in/')
driver.maximize_window()

time.sleep(3)
driver.execute_script("window.scrollBy(0, 500);")

driver.find_element_by_css_selector("img[alt='Selenium Ruby']").click()

time.sleep(3)
driver.find_element_by_class_name("reviews_tab").click()

# five stars rating
stars = driver.find_element_by_class_name("star-5").click()

# provide review
review = driver.find_element_by_css_selector("textarea#comment")
review.send_keys("Nice Book! " + str(time.time())) # the same text is not allowable for comment, added current timestamp

name = driver.find_element_by_css_selector("input#author")
name.send_keys("Name")

email = driver.find_element_by_css_selector("input#email")
email.send_keys("my@mail.ru")

# send review
driver.find_element_by_css_selector(".form-submit>input#submit").click()

# scroll for review check
comments = driver.find_element_by_id("comments")
driver.execute_script("return arguments[0].scrollIntoView(true);", comments)

time.sleep(3)
driver.quit()

