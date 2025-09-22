# scrape js content with selenium and geckodriver

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

url = 'https://www.kaggle.com/datasets?search=Data+Visualization'
print(url)

driver = webdriver.Firefox()

driver.get(url)
time.sleep(5)
page = driver.page_source
driver.quit()

soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())

# div classes retrieved with Inspect->right-click copy CSS selector
print(*soup.select('div.sc-fbQrwq.sc-fGqoZs.cecTRc.kXVPAX'), sep='\n')

