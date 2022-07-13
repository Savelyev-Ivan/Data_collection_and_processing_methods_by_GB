
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.ui import Select
load_dotenv()

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("https://gb.ru/login")

input = driver.find_element(By.ID, "user_email")
email = os.getenv("user_email")
input.send_keys(email)

input = driver.find_element(By.ID, "user_password")
password = os.getenv("user_password")
input.send_keys(password)
input.send_keys(Keys.ENTER)

profile = driver.find_element(By.XPATH, "//a[contains(@href,'/users/')]")
href = profile.get_attribute("href")
driver.get(href)

profile = driver.find_element(By.CLASS_NAME, "text-sm")
href = profile.get_attribute("href")
driver.get(href)

timezone = driver.find_element(By.NAME, "user[time_zone]")
select = Select(timezone)
select.select_by_value("Vladivostok")

timezone.submit()

print()
#driver.execute_script("")

#driver.close()