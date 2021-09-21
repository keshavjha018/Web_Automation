#Evertime this program takes message and no of messages to be sent as input
#            and sends them via whatsapp to specified contact
#                    (Runs as many times user want)

from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe' #location of chrome driver in local system
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys  #importing keys- select, click, Enter
import time

from datetime import datetime   #for printing current time

driver.get("https://web.whatsapp.com/")     #goto this page
print("-------------------------WHATSAPP BOMBER---------------------")
print("Scan the QR code to Log in...")
time.sleep(10)      #wait for QR code to be scanned by user...

#function to find contact in chat list,
# (must be saved in device contact list, else give phone number with country code)
def Selectcontact(name):

    css_path = 'span[title="' + name + '"]'
    name = driver.find_element_by_css_selector(css_path)
    name.click()

#function to send message
def sendMsg(message):
    chatbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]') #finds the chatbox
    chatbox.send_keys(message) #types the message
    chatbox.send_keys(Keys.RETURN) #press Enter

yesno = "y"
while yesno == 'y':
    
    #taking user inputs
    nameofcontact = input('Give name of contact: ')
    msg = input("Type the message you want to send: ")
    noofMsg = int(input("Give total no of messages to be sent: "))
    timegap = int(input('Give time gap bw messages (in Seconds): '))

    Selectcontact(nameofcontact)    #opens chat of given contact

    for i in range(noofMsg):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        sendMsg(msg + " Message sent at > " + current_time) #sends message with current time stamp
        time.sleep(timegap) #wait for given time gap

    yesno = input('Do you want to continue (Y/N): ').lower()

driver.quit()  #quit window