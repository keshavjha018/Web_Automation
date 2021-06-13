from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys
import time 

driver.get('https://www.testandquiz.com/selenium/testing.html')

driver.find_element_by_link_text('This is a link').click()