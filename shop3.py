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
book = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product/android-quick-start-guide/"]').click()
price = driver.find_element_by_css_selector("del>:nth-child(1)")
price_get_text = price.text
assert price_get_text == "₹600.00"
price2 = driver.find_element_by_css_selector("ins>:nth-child(1)")
price2_get_text = price2.text
assert price2_get_text == "₹450.00"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
button = WebDriverWait(driver, 5).until(
EC.element_to_be_clickable((By.CLASS_NAME, "images"))).click()
close = WebDriverWait(driver, 5).until(
EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
driver.quit()




