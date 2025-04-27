
#取網頁
from selenium  import webdriver

#存圖片
import os

#取元素
import requests

#讀取網頁元素
from bs4 import BeautifulSoup

#讀取圖片，但無法實際看到圖片內容
from selenium.webdriver.common.by import By


url = 'https://www.nike.com/tw/'
driver = webdriver.Chrome()

driver.get(url)

# htmlfile = driver.page_source

# soup= BeautifulSoup(htmlfile,'html.parser')
# img = soup.find_all('img')
# print(img)

imgs = driver.find_elements(By.TAG_NAME,'img')

print(imgs)



#抓圖 ，被鎖定之前沒有辦法抓檔案


