import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()
driver.execute_script("window.scrollBy(0, 300);")
buy1 = driver.find_element_by_css_selector('[data-product_id="182"]').click()
basket = driver.find_element_by_id('wpmenucartli').click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
btn1 = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward"))).click()
fn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
fn.send_keys("Vasya")
ln = driver.find_element_by_id('billing_last_name')
ln.send_keys("Pupkin")
email = driver.find_element_by_id('billing_email')
email.send_keys("VasyaPupkin@mail.com")
phone = driver.find_element_by_id('billing_phone')
phone.send_keys("1234567890")
country = driver.find_element_by_id('select2-chosen-1').click()
country1 = driver.find_element_by_id('s2id_autogen1_search')
country1.send_keys("germany")
country3 = driver.find_element_by_class_name('select2-match').click()
address = driver.find_element_by_id('billing_address_1')
address.send_keys("ulica pushkina dom kalatushkina")
zip = driver.find_element_by_id('billing_postcode')
zip.send_keys("80331")
city = driver.find_element_by_id('billing_city')
city.send_keys("Munchen")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
radiobutton = driver.find_element_by_id('payment_method_cheque').click()
btn2 = driver.find_element_by_id('place_order').click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
some_element= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce > p"), "Thank you. Your order has been received."))
some_element1= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>:nth-child(3)"), "Check Payments"))
driver.quit()









