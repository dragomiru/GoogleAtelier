from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import exceptions as exceptions
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()
# date = browser.find_element(by=By.XPATH, value='//*[id="card_grid"]')
date = browser.find_elements(by=By.CLASS_NAME, value='card-v2')
for i in date:
    try:
        title_of_product = i.find_element(by=By.CLASS_NAME, value='card-v2-title')
        print(title_of_product.text)
        price = i.find_element(by=By.CLASS_NAME, value='card-v2-pricing')
        print(price.text)
    except (exceptions.StaleElementReferenceException, exceptions.NoSuchElementException):
        pass
time.sleep(10)