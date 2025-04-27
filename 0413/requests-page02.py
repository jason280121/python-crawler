import requests
import bs4

# 解析網址
url = 'https://www.ptt.cc/bbs/gossiping/index.html'
# get 一般請求
# post 表單使用
# put 更新資料，全部修正更新
# patch 更新資料，局部更新
# delete  刪除


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}


# 基本讀取網頁
# data01 = requests.get(url)
# data02 = data01.text
# print(data02)
# print(data01.text)


# 有加Header user-agent 瀏覽器
data01 = requests.get(url, headers=header)

# 有加瀏覽器讀取網頁
data02 = data01.text
# print(data02)
# print(data01.text)


# 解析網頁資料
htmlfile = bs4.BeautifulSoup(data02, 'html.parser')
# find_all() 容器
titles = htmlfile.find_all('div', class_='title')
# 測試是否讀取所有title解析資料
# print(titles)


# for title in titles:
# 只有印出一頁的title
# print(title)
# 只印出title 文字
# print(title.a.string)

# 印出全部的title
# print(titles)


for title in titles:
    # print(title)
    if title.a is None:
        print("本文已刪~")
    else:
        print(title.a.string)
