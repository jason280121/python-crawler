
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
# img = soup.find_all('img')
imgs = soup.find_all('img')

# print(img)
i =1
for img in imgs :

    # print(img['data-landscape-url'])

    #路徑
    path =img['data-landscape-url']
    #取得圖片路徑
    source = requests.get(path)
    #取得內容
    img_source = source.content

    #創立資料夾
    os.makedirs('images',exist_ok=True)
    # os.makedirs('images', exist_ok=False)

    #wb 二進位寫入
    #w 取得網頁文字, 沒有二進制的問題
    #a 都寫入
    with open(f'images/{i}.jpg','wb') as f :
        f.write(img_source)

    i+=1



