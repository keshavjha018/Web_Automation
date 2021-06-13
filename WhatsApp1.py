from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys
import time 

driver.get("https://web.whatsapp.com/")
    #input("Scan QR and enter any key: ")

time.sleep(6)

def Selectcontact():

    name = driver.find_element_by_css_selector('span[title="+91 95232 07394"]')
    name.click()

def sendMsg():
    chatbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    chatbox.send_keys('Hello! this is a bot command')
    chatbox.send_keys(Keys.RETURN)

Selectcontact()
sendMsg()