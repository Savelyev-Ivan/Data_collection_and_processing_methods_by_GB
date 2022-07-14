import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError as dke
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)

db = client['trend_of_mvideo']
trends = db.trends

driver = webdriver.Chrome()
driver.get('https://mvideo.ru')

driver.implicitly_wait(10)

element = driver.find_element(By.TAG_NAME, 'mvid-shelf-group')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button/div/span[@class='title'" " and contains(.,'В тренде')]/../.."))).click()



names = driver.find_elements(By.XPATH, "//mvid-shelf-group/mvid-carousel/div/div/mvid-product-cards-group/div["
                                       "contains(@class, 'name')]")
prices = driver.find_elements(By.XPATH, "//mvid-shelf-group/mvid-carousel/div/div/mvid-product-cards-group/div["
                                        "contains(@class, 'price')]")

for name, price in zip(names, prices):
    price = float(re.match(r'\d+', price.text.replace(' ', ''))[0])
    name = name.text
    product = {
        'name': name,
        'price': price
    }

    db.trend_products.update_one({'name': name}, {'$set': product}, upsert=True)