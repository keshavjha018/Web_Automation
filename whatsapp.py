# This bot takes message and no of messages to be sent as input
# and sends them via whatsapp to specified contact
#(Runs for one time only)

from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys
import time
#for printing current time
from datetime import datetime

driver.get("https://web.whatsapp.com/")
    #input("Scan QR and enter any key: ")

#time.sleep(10)
nameofcontact = input('Give name of contact: ')
msg = input("Type the message you want to send: ")
noofMsg = int(input("Give total no of messages to be sent: "))
timegap = int(input('Give time gap bw messages (in Seconds): '))

def Selectcontact(name):

    css_path = 'span[title="' + name + '"]'
    name = driver.find_element_by_css_selector(css_path)
    name.click()

def sendMsg(message):
    chatbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    chatbox.send_keys(message)
    chatbox.send_keys(Keys.RETURN)

Selectcontact(nameofcontact)

for i in range(noofMsg):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    sendMsg(msg + " Message sent at > " + current_time)
    time.sleep(timegap)

driver.quit()