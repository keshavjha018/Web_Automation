from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
import time

from selenium.webdriver.common.keys import Keys

driver.get("https://twitter.com")

loginoption = driver.find_element_by_partial_link_text("Log in")
loginoption.click()

username = driver.find_elements_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")
username.send_keys("username")

password = driver.find_elements_by_xpath("//input[@type='password']")
password.send_keys("password")

loginbutton = driver.find_elements_by_xpath("//div[@class='css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-1fz3rvf r-usiww2 r-1pl7oy7 r-snto4y r-icoktb r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr']//div[@class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-b88u0q r-1777fci r-rjixqe r-dnmrzs r-bcqeeo r-q4m81j r-qvutc0']")
loginbutton.click()

# searchbox = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/label[1]/div[2]/div[1]/input[1]")
# searchbox.send_keys("Manoj Bajpayee")
# searchbox.send_keys(Keys.RETURN)

# name = driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/span[1]/span[1]")
# name.click()