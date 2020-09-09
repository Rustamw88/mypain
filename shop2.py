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
element = driver.find_element_by_tag_name("select").click()
element1 = driver.find_element_by_css_selector("[value='price-desc']")
element1.get_attribute("selected")
if element is not None:
    print("Выбрана сортировка от большего к меньшему")
else:
    print("Выбрана другая сортировка")
element2 = driver.find_element_by_css_selector("select>:nth-child(6)").click()
element = driver.find_element_by_tag_name("select")
element1 = driver.find_element_by_css_selector("[value='price-desc']")
element1.get_attribute("selected")
if element is not None:
    print("Выбрана сортировка от большего к меньшему")
else:
    print("Выбрана другая сортировка")
driver.quit()









