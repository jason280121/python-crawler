import time

from openpyxl.styles.builtins import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 男
url = 'https://www.nike.com/tw/w/mens-apparel-6ymx6znik1'
# 女
# url ='https://www.nike.com/tw/w/womens-apparel-5e1x6z6ymx6'
driver = webdriver.Chrome()
driver.get(url)

# 視窗最大化，因使用手機網頁
# driver.maximize_window()


# 15:00
n = 0
while n < 3:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight-1000)')
    time.sleep(5)
    n += 1

titles = driver.find_elements(By.CLASS_NAME, '.product-card__link-overlay')
# titles = driver.find_elements(By.CSS_SELECTOR,'.product-card__titles')


for title in titles:
    print(title.text)

time.sleep(3)
