#Get your attendance status screenshot 
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
_TOKEN = "Bot Token HERE"


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
    
def send_photo(chat_id, image_path, image_caption=""):
    data = {"chat_id": chat_id, "caption": image_caption}
    url = f'https://api.telegram.org/bot{_TOKEN}/sendPhoto'
    with open(image_path, "rb") as image_file:
        ret = requests.post(url, data=data, files={"photo": image_file})
        print(ret.text)
    return ret.json()

