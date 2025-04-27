import bs4
import urllib.request as req

# 說明
# ppt 八卦
# 18禁
# 記錄 cookie
# 右鍵，檢查cookie  over18


# 解析網址
url = 'https://www.ptt.cc/bbs/gossiping/index.html'


# 網頁表頭header
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 第一種方式只有over18=1
    'cookie': 'over18=1'
    # 第二種方式所有cookie 全部載入進來
    # 'cookie' : '_gid=GA1.2.1539988763.1744375860; cf_clearance=IoiSzMLd6np4VBdTIBf1clbRDQG4cJo.B0MB2FWNeJw-1744508002-1.2.1.1-R.l3_8cJQNyq5kfXao2wqpHO6bZExUTT1M9lSkXjeDUzVLtKbODGYja9dfLANqbYOxXgyAfQbFVkkb5DyH0vytJkBUEkJeGh50iJQpgLJRCrjml0lpt8_pWrCZagTy11SbG9s4JnZbwD.cLIT5Q2O6nvG2Jm9zK0VeBmwiMBi3GKjhd_PWbMQ.XOhSqtJ_jrOK2firWTUtw1MLK6Bl0VtnMefixvUxVAYIYcTX__OmThrSpJ.hNez2W3ITjQOZCgh5J3jLkNs44selRO8UlJi3os5_cOLtiy21jLy9D7vs7KpS0qy1ztNeSPugt88BrRBdfM7GEc5dg.EBAPCNk0hnRLyiPW_PVb6bMOMQjUbtk; over18=1; _ga_DZ6Y3BY9GW=GS1.1.1744508001.5.1.1744508015.0.0.0; _ga=GA1.1.1221673895.1744375860'
}


# 讀取網頁表頭資料
data = req.Request(url, headers=header)


# 打開網頁進行編碼
with req.urlopen(data) as response:
    # 使用response讀取網址內容，utf-8編碼
    datas = response.read().decode('utf-8')
# print(datas)

# with上述等同以下
# response = req.urlopen(data)
# datas = response.read().decode('utf-8')
# print(datas)


bs = bs4.BeautifulSoup(datas, 'html.parser')
# print(bs)
titles = bs.find_all('div', class_='title')
# print(titles)
for title in titles:
    # print(title)
    if title.a is None:
        print("本文已刪~")
    else:
        print(title.a.string)
