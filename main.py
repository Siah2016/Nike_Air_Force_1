from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Product ID - "div" product-card product-grid_card css-1x12eyj
# Name - product-card_title
# Gender - product-card_subtitle
# Color - product-card__colorway-btn
# Price - product-price us_styling is--current-price css-11s12ax

file = open("nike_shoes.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Name, Gender", "Color", "Price"])

browser_driver = Service("chromedriver.exe")
scrap = webdriver.Chrome(service=browser_driver)
scrap.get("https://www.nike.com/w/air-force-1-shoes-5sj3yzy7ok")

cookies = WebDriverWait(scrap, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'acceptCookies')))
cookies.click()

while True:
    Product_id = scrap.find_elements(By.CLASS_NAME, "product-card__body")

    for nike in Product_id:
        print(nike.text)
    