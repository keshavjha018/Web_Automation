#search for my username on google - and - open my quora account

from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver.get('https://www.google.com')

searchbox = driver.find_element_by_name("q")
searchbox.send_keys("keshavjha018")
searchbox.send_keys(Keys.ENTER)

link1 = driver.find_element_by_partial_link_text('Quora')
link1.click()