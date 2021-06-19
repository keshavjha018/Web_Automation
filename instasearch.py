from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
import time 
from selenium.webdriver.common.keys import Keys

driver.get("https://www.google.com")

searchbox = driver.find_elements_by_css_selector("input[title='Search']")
for inputElem in searchbox:

	inputElem.send_keys('nshotphoto')

	# Hits Enter Key
	inputElem.send_keys(Keys.ENTER)

findlink = driver.find_element_by_partial_link_text('Instagram photos')
findlink.click()