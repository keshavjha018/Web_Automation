#bot to read a blog automatically

from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys
import time 

driver.get('https://theknowledgefeed.blogspot.com/')
time.sleep(1)

searchbutton = driver.find_element_by_css_selector('body > div.page > div > div > header > div > div.search > button > svg')
searchbutton.click()
time.sleep(1)

searchbox = driver.find_element_by_css_selector("input[placeholder='Search this blog']")
searchbox.send_keys('Powerful')
searchbox.send_keys(Keys.RETURN)

time.sleep(1)

link = driver.find_element_by_partial_link_text('POWERFUL THOUGHTS').click()
time.sleep(1)

# command to go to the bottom of a page
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")