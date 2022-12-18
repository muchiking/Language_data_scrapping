from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

driver = webdriver.Chrome(os.getenv("chromedriver"))
# Navigate to a website
driver.get("https://www.bible.com/bible/2926/GEN.1.ogkbible")

# Get an element on the page
element = driver.find_element(By.CLASS_NAME, "reader").text

# Extract the text from the element
# text = element.get_text()
print(element)
