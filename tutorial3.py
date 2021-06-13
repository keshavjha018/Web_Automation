from typing import KeysView
from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
import time

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support import expected_conditions as EC

# Navigating and clicking elements by link text

driver.get("https://getintopc.com/")
link = driver.find_element_by_link_text("Operating Systems")
link.click()

# try:
#     #wait for 10 sec to search for the elements
#     # (in case if it is not found, it will quit)
#     element = WebDriverWait(driver,10).untill(
#         EC.presence_of_all_elements_located((By.LINK_TEXT, "Windows 8.1 Pro MAY 2021 Free Download"))
#     )
#     element.click()

# # if that element is not found the page will quit
# finally:
#     time.sleep(7)
#     driver.quit()

link2 = driver.find_element_by_link_text('Windows 8.1 Pro MAY 2021 Free Download')
link2.click()