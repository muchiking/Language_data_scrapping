from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import os
from urllib.request import urlretrieve
from dotenv import load_dotenv
import time
# import pandas as pd





load_dotenv()

def clone(num,book): 
    # df = pd.read_excel('genesis.xlsx')
    s=Service(os.getenv("chromedriver"))
    chrome_options = Options()
    options=chrome_options
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=s,options=chrome_options)
    # driver = webdriver.Chrome(options=chrome_options)
    driver.get(f"https://www2.bible.com/bible/2926/GEN.{num}.OGKBIBLE?show_audio=1")
    # driver.implicitly_wait(200)
    delay = 3600

    try:
        element = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/div[2]/div/audio/source[1]')))
        
        
    finally:
        text = driver.find_element(By.CLASS_NAME, "reader").text
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
        # with open("output1.html", "w", encoding='utf-8') as file:
        #     file.write(str(soup))
        images = soup.findAll('source')
        print(type(images))
        car=[]

        for image in images:
        # Print image source
            car+=[(image['src'])]
            # print(image['src'])
            print(car)
        # Print alternate text
        # print(image['alt'])
        sound=str(car[1])
        url="https:"+sound
        # os.system(f"aria2c -o {book}{str(num)}.mp3 -d sound/ {url}")
        name="chapters/"+book+" "+str(num)
        data = {
        "Book": name,
        "Text": text
        }
        f = open(name, "w")
        f.write(text)
        f.close()
        driver.quit()

book="Genesis"
for num in range(6,50):
# number=1
    clone(num,book)
# r = requests.get("https://www2.bible.com/bible/2926/GEN.1.OGKBIBLE?show_audio=1")    
#for element in thumbnail_elements:
#    print ("https://books.toscrape.com/" + element['src'])

# element = driver.find_element(By.CLASS_NAME, "reader").text
    
        # thumbnail_elements = soup.find_all("audio", class_ = "audio-player")
        # print(thumbnail_elements)
        # for element in thumbnail_elements:
        #     print (element['src'])