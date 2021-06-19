#this program will  login  to twitter.com
#with given user id and ppassword

from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys
import time 

email = 'Keshavjha018'
passw = 'passwordsa'

driver.get("https://twitter.com/login")

time.sleep(4)

userid_css = "#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input"
passw_css = "#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input"
login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span'

time.sleep(2)

userid = driver.find_element_by_css_selector(userid_css)
userid.send_keys("username")
time.sleep(1.5)
passw = driver.find_element_by_css_selector(passw_css)
passw.send_keys("Passsssss")
time.sleep(1)
driver.find_element_by_xpath(login_xpath).click()