from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import mysql.connector
from mysql.connector import errorcode
from database import cursor
from database import add_product

DB_NAME = "ikman_products"


driver = webdriver.Firefox()

driver.get("https://ikman.lk/en/ads/sri-lanka/electronics")


titles = driver.find_elements(By.CLASS_NAME, "heading--2eONR")

titleFile = open("titleFile.txt", "w")

for index, title in enumerate(titles, start=1):
    availability = 1
    product = title.text
    if index == 1:
        print(product)
    else:
        print(f"{index}. {product}")
        titleFile.write(f"{index}. {product} \n")
        add_product(index=index, product=product, availability=availability)

titleFile.close()


driver.quit()
