# evertime this bot takes message and no of messages to be sent as input
# and sends them via whatsapp to specified contact
#(Runs as many times user want)

from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys
import time
#for printing current time
from datetime import datetime

driver.get("https://web.whatsapp.com/")
print("Scan the QR code to Log in...")

def Selectcontact(name):

    css_path = 'span[title="' + name + '"]'
    name = driver.find_element_by_css_selector(css_path)
    name.click()

def sendMsg(message):
    chatbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    chatbox.send_keys(message)
    chatbox.send_keys(Keys.RETURN)

yesno = "y"
while yesno == 'y':
    
    nameofcontact = input('Give name of contact: ')
    msg = input("Type the message you want to send: ")
    noofMsg = int(input("Give total no of messages to be sent: "))
    timegap = int(input('Give time gap bw messages (in Seconds): '))

    Selectcontact(nameofcontact)

    for i in range(noofMsg):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        sendMsg(msg + " Message sent at > " + current_time)
        time.sleep(timegap)

    yesno = input('Do you want to continue (Y/N): ').lower()

driver.quit()