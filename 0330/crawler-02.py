
import urllib.request as req
import ssl

#內建模組urllib.request 請求網頁 req 別名

#資料抓回來
#會用到二個方法


#爬蟲一 ，抓取網路網頁資料
#輸入網址
# url = 'https://www.google.com/'
# url = 'https://www.momoshop.com.tw/main/Main.jsp?lpn=O1K5FBOqsvN&n=1&gid_ic=7435268ba8ec48963826efd4f01e7443&osm=iChannels&utm_source=CPA&utm_medium=iChannels&gad_source=1'
# url = 'https://www.tenlong.com.tw/'
# url = 'https://24h.pchome.com.tw/'

# url = 'https://www.ptt.cc/bbs/movie/index.html'
url = 'https://www.ptt.cc/bbs/movie/index10546.html'

#網頁，右鍵，檢查or F12 , 網路 ，F5 重整 ，找首頁，標頭或全部或文件，user-agent: '流覽器編碼'
request= req.Request(url, headers={
     'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'

 })
# print(data)


# 403 被阻檔
#404 不存在
# 500 後端server 問題
#200 開頭都是成功開啟網頁

#請求打開網址
# with req.urlopen(url) as response:
with req.urlopen(request) as response:
    #使用response讀取網址內容
    data = response.read()
    #utf-8編碼
    # data = response.read().decode('utf-8')
# print(data)


#13:36 開始
#安裝第三方模組，安裝套件
# pip  #測試之前是否有套件存在
#pip install beautifulsoup4
# python.exe -m pip install --upgrade pip    # 新版本不一定要裝

#爬蟲二 ，依據早上抓取網路網頁資料，以下做解析網頁資料
import bs4
#匯入beautifulsoup4

# 解析資料，解析器html
root = bs4.BeautifulSoup(data, 'html.parser')
# print(root)

#除錯
# titles = root.find('div',class_='title')
# print(titles)


#爬蟲三 ，抓網頁資料
# <a > 超連結,指示連結的目的地.
#div 區塊元素(block element)
#id  幫標籤取一個「專屬的名字」，只能用一次
#class  幫標籤貼上一個「分類」，可以重複使用
#title  網路標題, 元素定義了顯示在瀏覽器標題欄或頁面標籤上的文件標題。

# 操作: 點網路功能最左邊的 元素 ，會有底下html tag

# print(root.title) #網頁標題
# print(root.title.string)  #標題文字
# print(root.a)  #第一個連結
# print(root.a.string)  #第一個連結,文字

# test = root.find('a',class_='right small')
# test = root.find('a',class_='right')
# test = root.find('a',class_='small')
# print(test)

# title  = root.find('div',class_='title')
# print(title)
# print(title.a)
# print(title.a.string)

#尋找所有
# titles  = root.find_all('div',class_='title')
#find_all容器不能單獨使用
# print(titles.title)
# print(titles.a)
# print(titles.a.string)


# for title in titles:
#     #判斷也被刪除
#     if title.a is not None:
#         print(title.a.string)
#     else:
#         print('本文已被刪除')

# dates   = root.find_all('div', class_='date')
# for title in dates:
#     print(title.string)




#15:11
items = root.find_all('div',class_='r-ent')
for item in items:
    # print(item)
    #標題
    title  = item.find('div', class_='title')
    #日期
    date   = item.find('div', class_='date')
    #熱度
    nrec   = item.find('span', class_='hl')
    #作者
    author = item.find('div', class_='author')
    # if title.a is not None:
    #     print(title.a.string)
    # else:
    #     print("刪除")

    if nrec is None :
         nrec = '0'
    else:
        nrec= nrec.string

    if title.a is None:
        title = "本文已刪"
    else:
        title = title.a.string

    # print(f'{nrec.string}/{title.a.string} / {date.string}----{author.string}')
    print(f'{nrec:6}/{title:40} / {date.string:8}----{author.string:24}')


# 16:04
nextPage = root.find('a',string='‹ 上頁')
print(nextPage)
# print(nextPage['href'])
# return nextPage['href']








