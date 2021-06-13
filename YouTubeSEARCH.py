#Going to YouTube and searching

from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

driver.get('https://youtube.com')
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Bhakti songs')

searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')  
searchbutton.click()

#time.sleep(3)

videotoplay = driver.find_element_by_css_selector("yt-formatted-string[aria-label='BEAUTIFUL COLLECTION OF MOST POPULAR SHRI KRISHNA SONGS - HIT BHAJANS - BEST DEVOTIONAL SONGS by Supertone Digital 1 year ago 33 minutes 16,007,237 views']")
videotoplay.click
