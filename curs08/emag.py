from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import selenium.common.exceptions as exceptions
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument('start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.emag.ro/#opensearch')
get_element = driver.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()
element = driver.find_elements(by=By.CLASS_NAME, value='card-item')
product_list, price_list = [], []
list_of_elements = []
for i in element:
    try:
        product = i.find_element(by=By.CLASS_NAME, value='card-v2-title-wrapper')
        product_list.append(product.text)
        price = i.find_element(by=By.CLASS_NAME, value='product-new-price')
        price_list.append(price.text)
    except (exceptions.NoSuchElementException, exceptions.StaleElementReferenceException):
        pass

print(product_list, price_list)
list_of_elements.append(product_list)
list_of_elements.append(price_list)
df = pd.DataFrame(list_of_elements).transpose()
df.to_csv("emag_all_products.csv", sep='|')
