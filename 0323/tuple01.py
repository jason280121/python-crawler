
"""tuple() 集合課程程式碼"""


# tuple(), 使用小括號，括號內值不能變動
# ()
# <class 'tuple' >
# t1 = tuple()
# print(t1)
# print(type(t1))


# 讀取tuple()第一種寫法:
# (1, 2, 3, 4, 5)
t2 = (1, 2, 3, 4, 5)
# print(t1)


# tuple 讀取方式與list相同
# print(t1[0])  # 讀取索引0元素值
# print(t1[1])  # 讀取索引1元素值
# print(t1[2])  # 讀取索引2元素值
# print(t1[3])  # 讀取索引3元素值
# print(t1[4])  # 讀取索引4元素值

''' tuple (不能更動索引值), 會引發錯誤，
    但因不能更動，效率會比其它能更動的快 '''


# 更改tuple()索引值，引發錯誤
# t1[0] = 'A'

# tuple第二種寫法:
# (1, 2, 3, 4, 5)
# t3 = 1, 2, 3, 4, 5
# print(t1)

# tuple第三種寫法:
# (True, 'jason', 456, 0.9)
t4 = True, 'jason', 456, 0.9
# print(t2)


# 用第一種方式，使用 + 方式, tuple()串列與串列
# (1, 2, 3, 4, 5, True, 'jason', 456, 0.9)
# t5 = t2 + t4
# print(t5)


# 用第二種方式('apple',) 用+方式後面要加逗號
# (True, 'jason', 456, 0.9, 'apple')
# t4 = t4 + ('apple',)
# print(t4)


# 用第三種方式('apple'),未加逗號，型態為string
# apple
# <class 'str' >
# t6 = ('apple')
# print(t6)
# print(type(t6))

# 第一種轉換方式:tuple轉換成list
# [True, 'jason', 456, 0.9, 'jason']
# <class 'list' >
# t4 = list(t4)
# t4.append('jason')
# print(t4)
# print(type(t4))


# 第一種轉換方式:list轉tuple()型態
# (True, 'jason', 456, 0.9, 'jason')
# <class 'tuple' >
# t4 = tuple(t4)
# print(t4)
# print(type(t4))


# 第二種轉換 len()
# 4
# print(len(t4))

# 第三種轉換 index()
# 0.9 在索引的位置
# 3
# print(t4.index(0.9))

# 第四種轉換 count() ，計算串列中，'Hello'內容出現的次數
# 0
# 1
# print(t4.count('Hello'))  # 找不到索引值回傳 : 0
# print(t4.count(456))   # 找到回團索引位置

# 判斷式 in 判斷1 數值是否在t2 tuple元素內，判斷有:True , 無: False=0
print(2 in t2)
