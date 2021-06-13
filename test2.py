from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
import time 

#from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# If you have Chromedriver In Same folder then you dont need to pass executable path...
#driver = webdriver.Chrome(PATH)


driver.get('https://www.google.com')

#Sometimes Google Duplicates That Input Field So we have to iterate...

inputElems = driver.find_elements_by_css_selector("input[title='Search']")

for inputElem in inputElems:

	inputElem.send_keys('Search String...')

	# Presses Enter Key Like When You Press Enter Key to Search
	inputElem.send_keys(Keys.ENTER)