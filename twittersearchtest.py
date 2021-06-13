#this prog will search for my name on twitter and open my profile

from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
driver.get("https://twitter.com/elonmusk")
time.sleep(3)
searchbox = driver.find_element_by_css_selector("input[placeholder='Search Twitter']")
searchbox.send_keys("Keshavjha018")
searchbox.send_keys(Keys.RETURN)
time.sleep(4)
driver.find_element_by_partial_link_text("@Keshavjha018").click()