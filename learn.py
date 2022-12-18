from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from urllib.request import urlretrieve
from dotenv import load_dotenv
import time
load_dotenv()
s=Service(os.getenv("chromedriver"))
driver = webdriver.Chrome(service=s)
# Navigate to a website
driver.get("https://www2.bible.com/bible/2926/GEN.1.OGKBIBLE?show_audio=1")
# driver.implicitly_wait(200)
delay = 3 


# Get an element on the page that contains audio
# element = driver.find_element_by_id("some-element")
element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/div[2]/div/audio')#.get_attribute("src")
# element = driver.find_elements(By.tagName("audio"))#.get_attribute("src")
WebDriverWait(driver,30).until(
    EC.text_to_be_present_in_element_value(
        # Element filtration
        (By.CLASS_NAME,"progress-label"),"Complete!"
        # the expected text
    )
)
# Get the URL of the audio file
# audio_url = element.get_attribute("source")

# # Download the audio file
# urlretrieve(audio_url, "audio.mp3")
# print(audio_url)
print(element)


element_text = element.text
element_attribute_value = element.get_attribute('src')
print(element)
print('element.text: {0}'.format(element_text))
print('element.get_attribute(\'src\'): {0}'.format(element_attribute_value))


# for element in element :
#     print(element)