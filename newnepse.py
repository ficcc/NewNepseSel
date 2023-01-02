import pandas as pd
from selenium import webdriver
import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import Select

##Time
dsyr = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

##Driver

driver = webdriver.Chrome()

##Url

url = "https://newweb.nepalstock.com/today-price"
driver.get(url)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

dropdown = Select(driver.find_element_by_xpath("/html/body/app-root/div/main/div/app-today-price/div/div[2]/div/div[3]/select"))
dropdown.select_by_visible_text('500')
button = driver.find_element_by_xpath("/html/body/app-root/div/main/div/app-today-price/div/div[2]/div/div[4]/button[1]")
time.sleep(10)
button.click()
time.sleep(10)
html=driver.page_source
df = pd.read_html(html)
df[0].to_csv(dsyr +' '+ 'newnepse.csv',index = False)
print(df)
 ##BEautiful Soup

   




 
