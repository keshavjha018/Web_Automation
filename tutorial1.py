from os import path
from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://codenotesbykeshav.blogspot.com')

#prints page title on console and quit the site
print(driver.title)
driver.quit()