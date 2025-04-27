
# chrome driver
# google page chrome driver chrome15 查詢，設定，說明 , 關於
# chrome15 下載 chromedriver	win64	 下載，解壓縮，放在專案資料夾
# pychrom  專案資料夾，右鍵，openin , 匯入chromedriver.exe
# 套件下載  pip install selenium

import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# webdriver 啟動
driver = webdriver.Chrome()

# 輸入網址，打開瀏覽器
url = 'https://google.com'

driver.get(url)
# driver.get('https://24h.pchome.com.tw/')

# 視窗最大化，因使用手機網頁
# driver.maximize_window()


# 擷取瀏覽器，產生圖片
# driver.save_screenshot('google.jpg')
# driver.save_screenshot('pchome.jpg')

# 搜尋
# google.com   網址:  textarea


time.sleep(3)
search = driver.find_element(By.CLASS_NAME, 'gLFyf')
time.sleep(2)
search.send_keys('午')
time.sleep(1)
search.send_keys('飯')
time.sleep(4)
search.send_keys(Keys.ENTER)
time.sleep(9)
