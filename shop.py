import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
btn1 = driver.find_element_by_id('menu-item-50').click()
email = driver.find_element_by_id('username').send_keys("VasyaPupkin@mail.com")
password = driver.find_element_by_id('password').send_keys("VasyaPupkin123")
btn2 = driver.find_element_by_name('login').click()
shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()
btn = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product/html5-forms/"]').click()
element = driver.find_element_by_css_selector(".product_title.entry-title")
element_get_text = element.text
assert element_get_text == "HTML5 Forms"
driver.quit()