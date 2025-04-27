
s = 'Hello'

# len() 長度
# print(len(s))

#count() 計算字串中符合字元總數
# print(s.count('l'))

#index  查索引值位置
print(s.index('o'))

#find() 與index()差別:
#index()若找不到字串索引值會錯誤
# print(s.index('h'))
#find()若找不到字串索引值會回傳-1
# print(s.find('h'))



#isalpha()  判定字串內容是否為全文字
# print(s.isalpha())


#isdigit() 判定全數字(但還是以字串方式)
# s = '123'
# print(s.isdigit())



#endswith() 判斷最後一個索引值
# print(s.endswith('o'))

#startswith() 判斷開頭字
# print(s.startswith('H'))


#print("----------下午上課--------------")

# s = 'hello world'
#upper() 將文字小寫轉換成大寫
# print(s.upper())

#lower() 所有大寫字母轉換成小寫字母
# s = 'HELLO WORLD'
# print(s.lower())


#capitalize()  第一個字元轉換為大寫，並將所有其他字元轉換為小寫
# print(s.capitalize())

#title() 第一個字母大寫，其餘小寫
# print(s.title())

# s2= 'hello jason'
#replace() 取代  old舊的字串:jason , 產生新的字串，new:jjj
# print(s2.replace('jason','jjj'))


#split()  切割符號
# q = s2.split()
# q =s2.split('o')
# print(type(s2))

# print(q)
# print(type(q))

# print(s2.split())

#strip()  去除(左右邊)空白符號
# s3 = '   hello   '
# print(s3.strip())

#去除(左邊)空白符號
# print(s3.lstrip())

#去除(右邊)空白符號
# print(s3.rstrip())



