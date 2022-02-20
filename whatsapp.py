from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 

CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\Chaitanya\\AppData\\Local\\Google\\Chrome\\User Data\\whatsapp_noqrpythoncode"

name= input("Enter the recipient's/group's name:")
msg=input('Enter the message to be sent:')
count= int(input('Enter the number of times the message needs to be sent:'))

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

driver = webdriver.Chrome(
    executable_path='C:\\Users\\Chaitanya\\AppData\\Roaming\\Python\\Python310\\site-packages\\chromedriver', options=options)

driver.maximize_window()

driver.get('https://web.whatsapp.com/')

time.sleep(30)

user= driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box= driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/div[1]/div[2]/div[1]/div/div[2]")

for index in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/div[1]/div[2]/div[2]/button").click()
    
