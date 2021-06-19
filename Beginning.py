#Going to YouTube and searching

from selenium import webdriver
#the following command helps to run  the code without cmd
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
import time

#going to a website
driver.get('https://youtube.com')

#Finding the searchbox on the website
searchbox = driver.find_element_by_xpath('//*[@id="search"]')  #here searchbox is a variable
#typing into the search Box
searchbox.send_keys('New Songs')

#Finding search icon to click
searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')  #searchbotton is a variable
#clicking on search icon to search
searchbutton.click()

#to close browser
#driver.quit()