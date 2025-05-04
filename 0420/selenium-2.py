import time

from openpyxl.styles.builtins import title
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
url = 'https://www.tenlong.com.tw/'


# url = 'https://www.funtime.com.tw/localtour/result.php?from_city=TY&target=CT_SEOUL&date_st=2025-05-30&date_ed=2025-06-27&type=pkg'

# time.sleep(1)

driver.get(url)
# selector 選取器
# tag 標籤 , div 會重覆
# class , class_=   可重覆
# id  唯一 ，

# 視窗最大化，因使用手機網頁
# driver.maximize_window()


# 天瓏書局
# titles =driver.find_elements(By.CLASS_NAME, 'title')
# print(title)
# for title in titles:
#     print(title.text)

# funtime網站, 讀取標題文字
# titles =driver.find_elements(By.CLASS_NAME, 'good_url')
# print(titles.text)
# # for jason in titles:
# #     print(jason.text)


# 天瓏書局 , 輸入文字地方 id
kw = driver.find_element(By.ID, 'keyword')
print(kw)


# 未用選取器
# ok
# titles=driver.find_elements(By.CLASS_NAME,'title')
# print(titles)
# for title in titles :
#     print(title.text)


# 選取器方式
# titles=driver.find_elements(By.CSS_SELECTOR,'.title')
# print(titles)
# for ti in titles:
#     print(ti.text)


# OK
# titles=driver.find_element(By.CSS_SELECTOR,'.keywords-list')
# print(titles)
# print(titles.text)
# titles=driver.find_elements(By.CSS_SELECTOR,'.keywords-list .mr-4' )
# titles=driver.find_elements(By.CSS_SELECTOR,'.keywords-list a' )
# for title in titles:
#     print(title.text)

# print(titles)


# TAG_NAME    # div h1 h2
# CLASS_NAME   # class
# ID           id

# 選取器
# .title
#  container
#  h4

time.sleep(4)
