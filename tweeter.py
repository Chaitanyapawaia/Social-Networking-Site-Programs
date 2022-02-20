from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome(executable_path='C:\\Users\\Chaitanya\\AppData\\Roaming\\Python\\Python310\\site-packages\\chromedriver')

driver.maximize_window()

driver.get('https://twitter.com/login')

user_id=input("Enter User Id :")
user_password =input("Enter User Password :")
user_tweet=input("Enter Tweet :")

tweetcount= int(input("Enter number of tweet :"))

time.sleep(5)

user= driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
user.click()
user.send_keys(user_id)

password= driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
password.click()
password.send_keys(user_password)

login= driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]')
login.click()



for repetition in range(0,tweetcount):
    
    time.sleep(5)
    
    tweet= driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
    tweet.click()

    tweet_text= driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
    tweet_text.click()
    tweet_val= user_tweet + str(repetition)
    tweet_text.send_keys(tweet_val)

    tweet_send= driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]')
    tweet_send.click()

