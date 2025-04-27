
""""set 集合課程程式碼"""


# set無序，資料不重覆(重覆會自動移除)
# 原始資料保留，不能更動tuple()，一般最整理後資料比對
# list 自由度高，有序，可更改元素值


# set 資料不可重覆，宣告方式使用{}大括孤
# (去掉重覆資料使用)，舉例:調用資料如: 認領動物資料，會有重覆資料時
# {1, 2, 3}
# <class 'set' >
# s1 = {1, 2, 3}
# print(s1)
# print(type(s1))

# 宣告set{}，去除重覆資料，避免重覆資料產生
# {1, 2, 3}
# s1 = {1, 2, 2, 2, 2, 2, 3}
# print(s1)


# 字典:大括號前未寫變數，宣告方式為:字典dict
# {}
# <class 'dict' >
# s2 = {}
# print(s2)
# print(type(s2))


# 建立set空集合(未給)初始值，會產生錯誤
# s2 = set{}  # 空set未給元素初始值會出現錯誤
# s2 = {1, 2, 3}
# print(s2)


# set{}去掉重覆索引值
# {'台中市', '台北市', '桃園市', '新竹市'}
l1 = ['台北市', '台北市', '桃園市', '桃園市', '桃園市', '桃園市', '新竹市', '新竹市', '台中市']
city = set(l1)
# print(city)


# set{} 轉list型態
# ['新竹市', '桃園市', '台北市', '台中市']
# <class 'list' >
# city = list(city)
# print(city)
# print(type(city))


# set 轉 tuple()型態
# ('新竹市', '台中市', '台北市', '桃園市')
# <class 'tuple' >
# city = tuple(city)
# print(city)
# print(type(city))


# set{}加入元素值
# {1, 2, 3, '台中市', '花蓮市'}
s1 = {1, 2, 3, '花蓮市', '台中市'}
# print(s1)


# set{} add() 插入元素值,插入元素位置是隨機，不固定
# {'台中市', 2, 3, 1, 4, '花蓮市'}
# <class 'set' >
# s1.add(4)
# print(s1)
# print(type(s1))


# set{}, remove()刪除時，會報錯誤訊息
# s1.remove(5)

# set{}, discard()刪除時，不會回報錯誤訊息
# s1.discard(5)


# set{}, pop()隨機刪除, 測試只會刪除一個元素值
# s1.pop()


# 集合的相加 s1 + city
# {1, 2, 3, '新竹市', '花蓮市', '台中市', '桃園市', '台北市'}
# s1.update(city)
# print(s1)

# set{}  清除 clear()
# set()
# s1.clear()
# print(s1)

# set 使用交集、聯集，差集 ， 無新:無索引
se1 = {1, 2, 3, 4, 5}
se2 = {4, 5, 6, 7, 8}

# 聯集後，去除重覆性
# {1, 2, 3, 4, 5, 6, 7, 8}
# 聯集使用 |
# result = se1.union(se2)
# result = se1 | se2
# print(result)


# 交集，重覆性value
# {4, 5}
# 交集使用 &
# result = se1.intersection(se2)
# result = se1 & se2
# print(result)


# 差集(左)se1
# {1, 2, 3}
# 差集左使用 -
# result = se1.difference(se2)
# result = se1 - se2
# print(result)

# 差集(右) se2
# {8, 6, 7}
# 差集右使用 -
# result = se2.difference(se1)
# result = se2 - se1
# print(result)

# 對稱差集
# {1, 2, 3, 6, 7, 8}
# result = se1.symmetric_difference(se2)
# result = se1 ^ se2
# print(result)

# in 判斷
# False
# True
print(6 in se1)
print(6 in se2)
