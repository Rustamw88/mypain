import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()
buy = driver.find_element_by_css_selector('[data-product_id="182"]').click()
element1 = driver.find_element_by_css_selector('.wpmenucartli.wpmenucart-display-standard.menu-item')
element1_get_text = element1.text
assert "1 Item" in element1_get_text
element = driver.find_element_by_class_name("amount")
element_get_text = element.text
assert "₹180.00" in element_get_text
element.click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
some_element11 = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-Price-amount.amount"), "180.00"))
driver.quit()
