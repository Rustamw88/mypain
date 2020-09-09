import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()
driver.execute_script("window.scrollBy(0, 300);")
buy1 = driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(5)
buy2 = driver.find_element_by_css_selector('[data-product_id="180"]').click()
basket = driver.find_element_by_id('wpmenucartli').click()
time.sleep(5)
delete = driver.find_element_by_css_selector('[data-product_id="182"]').click()
undo = driver.find_element_by_css_selector('.woocommerce-message>:nth-child(1)').click()
clear = driver.find_element_by_name('cart[045117b0e0a11a242b9765e79cbf113f][qty]').clear()
window1 = driver.find_element_by_name('cart[045117b0e0a11a242b9765e79cbf113f][qty]')
window1.send_keys("3")
btn1 = driver.find_element_by_name('update_cart').click()
element = driver.find_element_by_name('cart[045117b0e0a11a242b9765e79cbf113f][qty]')
element_check = element.get_attribute("value")
assert element_check == "3"
time.sleep(5)
btn2 = driver.find_element_by_name('apply_coupon').click()
element2 = driver.find_element_by_class_name("woocommerce-error")
element2_get_text = element2.text
assert "Please enter a coupon code." in element2_get_text
driver.quit()