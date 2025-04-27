
#取網頁
from selenium  import webdriver
#存圖片
import os
#取元素
import requests


#抓圖 ，被鎖定之前沒有辦法抓檔案
from bs4 import BeautifulSoup


url = 'https://www.nike.com/tw/'
driver = webdriver.Chrome()

driver.get(url)


#獲取html訊息
htmlfile = driver.page_source
# print(htmlfile)

soup= BeautifulSoup(htmlfile,'html.parser')
img = soup.find_all('img')

print(img)





