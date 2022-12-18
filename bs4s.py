from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import threading
chrome_options = Options()
import os
from urllib.request import urlretrieve
from dotenv import load_dotenv
import time
# import pandas as pd
chrome_options.add_argument("--headless")




load_dotenv()

def clone(num,book,scope): 
    s=Service(os.getenv("chromedriver"))
    chrome_options = Options()
    options=chrome_options
    chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(service=s,options=chrome_options)
    driver = webdriver.Chrome(service=s)
    driver.get(f"https://www2.bible.com/bible/1810/{scope}.{num}.dho15?show_audio=1")
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
        os.system(f"aria2c -o {book}{str(num)}.mp3 -d sound/ {url}")
        # name=book+" "+str(num)
        name="chapters/GEN/"+book+" "+str(num)
        data = {
        "Book": name,
        "Text": text
        }
        f = open(name, "w")
        f.write(text)
        f.close()
        driver.quit()


book1=("Samuel","Jeremiah","Isaya")
scope1=("1SA","JER","ISA")
end=(31,52,65)
t=threading.Thread()
# for num in book1:
for num in range(len(book1)):
    print(num)
    current_book=book1[num]
    print(current_book)
    fin=end[num]
    url=scope1[num]
    # thread1 = threading.Thread(target = clone, args = (10,'thread1', ))
    for num1 in range(1,fin):
        # clone(num1,book=current_book,scope=url)
        thread1 = threading.Thread(target = clone, args = (num1,current_book,url,))
        thread1.start()
        thread1.join()
# r = requests.get("https://www2.bible.com/bible/2926/GEN.1.OGKBIBLE?show_audio=1")    
#for element in thumbnail_elements:
#    print ("https://books.toscrape.com/" + element['src'])

# element = driver.find_element(By.CLASS_NAME, "reader").text
    
        # thumbnail_elements = soup.find_all("audio", class_ = "audio-player")
        # print(thumbnail_elements)
        # for element in thumbnail_elements:
        #     print (element['src'])