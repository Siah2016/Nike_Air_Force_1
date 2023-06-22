from bs4 import BeautifulSoup
import requests
import csv

# Product ID -
# Name - 
# Gender - 
# Color - 
# Price - 

file = open("nike_shoes.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Name, Gender", "Color", "Price"])

page = requests.get("https://www.nike.com/w/air-force-1-shoes-5sj3yzy7ok")
soup = BeautifulSoup(page.text, "html.parser")

product_id = soup.find_all()