

#git-scm 上網下載 github  Git-2.49.0-64-bit.exe
# https://git-scm.com/downloads/win
# gitHub version Control 版本控制, 如紀錄點

#git  版本控制 ，儲存庫，公開，協作，開放別人共享
#gitHub 雲端，給git專用，多人協作位置
#git-lab 另外
#bit-bucket 另外


#本地端
#修改，新增，刪除，更新，先放置暫存區，上傳到暫存區



#暫存區
#暫存區如果覺的沒有問題的話，然後在放置儲存庫


#儲存庫
#放置儲存庫就會有一個紀錄點，可以回到之前的紀錄點，存檔，管控版本


# widows + r
#cmd
#git -v
# (git version 2.49.0.windows.1)



#桌面路徑
# C:\Users\jason58.tsou\
#mkdir 0427
#cd 0427

#建立初始化git 資料夾
#git init

# 備註說明:
#.git 版本隱藏檔，不能刪除

# 11:40

#查看設定值
#git config --list

#完整寫法 二個底線--
#設定電子郵件
#git config --global user.email jason58.tsou@gmail.com

#設定名字
#git config --global user.name jason280121


#實際流程 11:59
#查詢狀態(紅色，本地端)
#git status
#Untracked files 未追縱檔案，還在存本地端檔案 ，新增

#檔案加入暫存區(綠色)，單個檔案寫檔名.副檔名
#git add jason.txt

#資料夾所有紅色加入
#git add .

#儲存庫  ''空字串 -m(message)
# git commit -m ""
# git commit -m 20250427
# git commit -m "20250427 my first file"

#查看上傳紀錄
#git log

#重設專案 git init
#重開pycharm







#13:42 git回復
# git log --oneline

#看到所有,參照紀錄
#git reflog


#硬回復
# git reset *** --hard

#軟回復
#git reset *** --soft

#一般回復
#git reset ***


#14:23 上傳 ，進入git hub
# https://github.com/jason280121/0427.git

#檢查
#git status

#連線
# git remote add origin https://github.com/jason280121/0427.git

#查詢
#git remote

#把專案推上去 , origin連線, master(分支)
# git push origin master

#15:08
#push 上傳(上)

#pull 下載(拉)

#有專案時要用pull
#git pull origin master



#沒有專案時用clone(下載老師檔案)
#git clone 下載網址



#新建專案
#git remote add origin https://github.com/jason280121/python-crawler.git












































