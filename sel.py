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

def login(driver,username,password):
    driver.get('https://studentportal.hindustanuniv.ac.in/home.htm')
    driver.find_element(By.XPATH, '//*[@id="username_temp"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="form-password"]').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/form/button').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/ul/li[3]/a/i').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/ul/li[3]/ul/li[4]/a').click()
    width = 1500
    height = 2000
    driver.set_window_size(width, height)
    driver.get_screenshot_as_file("screenshot.png")
    send_photo('Chat_id','screenshot.png',"today's status")
    print('LOGGED IN...')
username = input('Enter your Username: ')
password = input('Enter your password: ')
login(driver,username,password)
driver.quit()
