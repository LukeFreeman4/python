import os
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random

#"/home/luke/Documents/Selenium/chromedriver.exe
os.environ['PATH'] += r"/home/luke/Documents/Selenium"
driver = webdriver.Chrome()


def scrape_Wiki_Articles():
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    response = driver.get(url)
    driver.implicitly_wait(3)
    my_element = driver.find_element(By.ID, 'firstHeading').text

    all_links = driver.find_elements(By.TAG_NAME, 'a')
    random_link = random.choice(all_links)
    link_to_scrape = random_link.get_attribute('href')
    print(link_to_scrape)
