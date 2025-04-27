import time

from openpyxl.styles.builtins import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.nike.com/tw/w/mens-apparel-6ymx6znik1'
driver = webdriver.Chrome()
driver.get(url)

# 視窗最大化，因使用手機網頁
# driver.maximize_window()


# titles = driver.find_elements(By.CLASS_NAME,'.product-card__link-overlay')
titles = driver.find_elements(By.CSS_SELECTOR, '.product-card__titles')

for title in titles:
    print(title.text)
