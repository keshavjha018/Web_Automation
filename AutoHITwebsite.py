#Opens, reads and closes the given blog in LOOP

from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys
import time 

def infiniteHits():
    driver.get('https://theknowledgefeed.blogspot.com/')
    time.sleep(1)

    searchbutton = driver.find_element_by_css_selector('body > div.page > div > div > header > div > div.search > button > svg')
    searchbutton.click()
    time.sleep(0.5)

    searchbox = driver.find_element_by_css_selector("input[placeholder='Search this blog']")
    searchbox.send_keys('Powerful')
    searchbox.send_keys(Keys.RETURN)

    time.sleep(0.5)

    Link = driver.find_element_by_partial_link_text('POWERFUL THOUGHTS').click()
    time.sleep(0.5)

    # command to go to the bottom of a page
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(0.5)
    driver.back()
    driver.back()
    driver.back()

for i in range(5):
    infiniteHits()