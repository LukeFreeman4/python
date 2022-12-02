import os
from  selenium import webdriver
from selenium.webdriver.common.by import By
import time

#"/home/luke/Documents/Selenium/chromedriver.exe
os.environ['PATH'] += r"/home/luke/Documents/Selenium"
driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")
driver.implicitly_wait(3)
my_element = driver.find_element(By.ID, 'js-link-box-en')
my_element.click()
driver.implicitly_wait(10)

