from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 
import random

driver = webdriver.Chrome(
    executable_path='C:/Users/Chaitanya/anaconda3/chromedriver')

driver.maximize_window()

driver.get('https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fwww.google.com%3Fhl%3Den-US&ec=GAlA8wE&flowName=GlifWebSignIn&flowEntry=AddSession')

time.sleep(5)

create= driver.find_element_by_xpath('//*[@id="ow324"]/span/span')
create.click()

time.sleep(1)

myself= driver.find_element_by_xpath('//*[@id="initialView"]/div[2]/div[2]/div/div/span[1]')
myself.click()

time.sleep(1)

us_val_opt='qwertyuioplkjhgfdsazxcvbnm'

firstname_val=''
for fn_seq in range(0,7):
    firstname_val=firstname_val + us_val_opt[random.randint(0, 25)]

firstname= driver.find_element_by_xpath('//*[@id="firstName"]')
firstname.click()
firstname.send_keys(firstname_val)

lastname_val=''
for ln_seq in range(0,7):
    lastname_val=lastname_val + us_val_opt[random.randint(0, 25)]

lastname= driver.find_element_by_xpath('//*[@id="lastName"]')
lastname.click()
lastname.send_keys(lastname_val) 

email_name=firstname_val+"."+lastname_val
email= driver.find_element_by_xpath('//*[@id="username"]')
email.click()
email.send_keys(email_name)

passwd_val_opt='qwertyuioplkjhgfdsazxcvbnm1234567890'

password_val=''
for ln_seq in range(0,9):
    password_val=password_val + passwd_val_opt[random.randint(0, 35)]

password= driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
password.click()
password.send_keys(password_val) 

con_password= driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
con_password.click()
con_password.send_keys(password_val)

next_1= driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/div[2]')
next_1.click()
