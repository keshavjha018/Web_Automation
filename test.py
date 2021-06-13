#testfile

from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
import time 
from selenium.webdriver.common.keys import Keys

driver.get("https://getintopc.com")

searchbox = driver.find_element_by_xpath('//*[@id="instance-atom-search-3"]/div/form/fieldset/input[1]')
searchbox.send_keys("Windows 10")
searchbox.send_keys(Keys.RETURN)