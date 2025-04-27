import time

from openpyxl.styles.builtins import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 男
# url ='https://www.nike.com/tw/w/mens-apparel-6ymx6znik1'
# 女
# url ='https://www.nike.com/tw/w/womens-apparel-5e1x6z6ymx6'

url = 'https://www.nike.com/tw/'
driver = webdriver.Chrome()
driver.get(url)

# 視窗最大化，因使用手機網頁
# driver.maximize_window()


# 16:05

# 連結文字
link = driver.find_element(By.LINK_TEXT, '男款')
# 點擊
link.click()
time.sleep(3)


link2 = driver.find_element(By.LINK_TEXT, '鞋款')
link2.click()

time.sleep(3)


info = driver.find_elements(By.CLASS_NAME, 'product-card__info')
time.sleep(3)


for item in info:
    # print(item.text)
    title = item.find_element(By.CLASS_NAME, 'product-card__title').text
    price = item.find_element(By.CLASS_NAME, 'product-card__price').text
    print(f'{title}:{price}')

time.sleep(8)

# 作業
# uniqo  放大鏡 ，key in , 抓資料
