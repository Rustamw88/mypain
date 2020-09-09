import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
btn = driver.find_element_by_tag_name('h3').click()
vkladka1 = driver.find_element_by_css_selector('[href="#tab-reviews"]').click()
stars = driver.find_element_by_class_name('star-5').click()
comment = driver.find_element_by_id('comment')
comment.send_keys("Nice book!")
name = driver.find_element_by_id('author').send_keys("Vasya Pupkin")
email = driver.find_element_by_id('email').send_keys("VasyaPupkin@mail.com")
btn1 = driver.find_element_by_id('submit').click()
driver.quit()


