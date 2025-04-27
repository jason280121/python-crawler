#有順序性，有索引, 可重覆

#建立空的list
# l1 = []

# []
# <class 'list'>
#建立空list, 型別轉換
# l1=list()
# print(l1)
# print(type(l1))




# ['apple ', 'banana', 'cat']
# <class 'list'>
# l1 = list(['apple ', 'banana','cat'])
# print(type(l1))




# ['apple', 123, 0.98, True, True, 123, 'hello']
# v1 = ['apple', 123,0.98,True, True,123, 'hello']
# print(v1)


# apple
# v1 = ['apple', 123,0.98,True, True,123, 'hello']
# print(v1[0])

# hello
# print(v1[-1])

# ['apple', 123, 0.98, True, True, 123]
# print(v1[0:6])

# ['apple', 123, 0.98]
# print(v1[:3])

# [0.98, True]
# print(v1[2:4])

#for 迴圈  知道範圍是多少(上限值)?
#for-loop 比較適用在「已知迴圈數」的問題
# apple 123 0.98 True True 123 hello
# for data in v1:
#     print(data)

# apple 123 0.98 True True 123 hello
# for i  in range(len(v1)):
#     print(v1[i])

# print("---------------0316 14:00 下午list[]-------------")


# l1 = ['apple', 123,0.98,True, True,123, 'hello']

#len()  查詢串列的長度
# 7
# print(len(v1))

#count() 快速取得串列中某個元素出現的次數。
# 2
# print(v1.count(123))

# index() 取得陣列元素的索引值
# 0
# print(v1.index('apple'))


# 14:55分

#extend() 插入最後面,只能加入串列，不可以是元素
#['apple', 123, 0.98, True, True, 123, 'hello', 'python', 'mysql']
# extend方法(只能加入串列，不可以是元素)。它會把串列中的元素做為個別元素加進串列裡
# v1.extend(['python','mysql'])
# v1.extend('python','mysql')  !會發生錯誤!
# print(v1)

#不正常，因list可跌帶會拆成個別元素
# v1.extend('python')

#正常插入
# v1.extend(['python'])

'''
如:
list = [1,2,3,4,5,6]
list.extend(10)      # 錯誤
list.extend([11,12])
print(list)

[1, 2, 3, 4, 5, 6, 11, 12]
'''

#append()  插入最後面, append方法的參數可以是元素也能是串列
# ['apple', 123, 0.98, True, True, 123, 'hello', 'python']
# v1.append('python')
#append() 插入二個，會變成二維list
# ['apple', 123, 0.98, True, True, 123, 'hello', ['python', 'mysql']]
# v1.append(['python','mysql'])
# print(v1)


#insert()  將元素放在指定的位置，原來的資料會自動往後退。
# ['apple', 123, 0.98, True, True, 123, 'hello']
# ['apple', 123, 'python', 0.98, True, True, 123, 'hello']
# print(v1)
# v1.insert(2,'python')
# print(v1)

#remove() 一次移除一個, (值), 一個以上remove('value')*2次
'''從第一項資料開始，找到指定資料，然後將它刪除。如果有多筆相同的資料，
   只會刪除第一個找到的資料。'''
# v1.remove(123)
# v1.remove(123)
# print(v1)

#pop() ，元素(索引值)
# ['apple', 123, 0.98, True, 123, 'hello']  刪除一個True
# v1.pop(3)
# print(v1)
''' 由串列中取出元素，同時串列會將該元素移除。pop方法可以
    有參數或是沒有，如果沒有就會拿掉最後一個元素;有參數，
    就會依照索引值去取出。'''


# [1, 2, 3, 5, 6]
# list1 = [1,2,3,4,5,6]
# list1.pop()
# print(list1)
# [1, 2, 3, 4, 5]  刪除索引元位值3
# list1.pop(3)
# print(list1)





#clear() 全部清空
# []
# v1.clear()
# print(v1)


# v1 = ['apple', 123,0.98,True, True,123, 'hello']

#sort()  要同型別才能排序
# [1, 2, 4, 6, 8]
# l2= [1,2,6,8,4]
# l2.sort()
# print(l2)


# ['1', '2', '3', '5']
# l3=['2','5','1','3']
# l3.sort()
# print(l3)


# [1.2, 5.2, 9]   浮點數排序
# l4 = [1.2,9,5.2]
# l4.sort()
# print(l4)


#sort(reverse=True)帶參數值(反轉排序)
# [8, 6, 4, 2, 1]
# l2= [1,2,6,8,4]
# l2.sort(reverse=True)
# print(l2)



#reverse() 反轉排序
# 5.2, 9, 1.2]  浮點數反轉排序
# l4 = [1.2,9,5.2]
# l4.reverse()
# print(l4)


# 15:50 分


#copy() 一般復製list
# c1= [1,2,3,4]
#拷貝一份過去
# c2 =c1.copy()
# c1[0] = 'A'
# c2[1] = 'B'
# print(c1)
# print(c2)

#共用同一個記憶體位址。
# c3 =c1

#資料分析，資料爬𠁷用(不到深層拷貝)
#深層拷貝(類神經網路與AI)

# c2 =c1.copy()
# c1[0]='A'

#深層烤貝，需import copy
# ['K', 2, ['M', 4]]
# [1, 2, [3, 4]]
# ['K', 2, ['M', 4]]
import copy
c1= [1,2,[3,4]]
c2= copy.deepcopy(c1)
c3 =c1
c1[0]= 'K'
c1[2][0]= 'M'

print(c1)
print(c2)
print(c3)


# c1[1]='J'
# c1[2][0]='A'


# c1[0] = 'H'
# c1[1] = 'p'

# print(c1[2][0])
# print(c1[2][1])





#淺層拷貝  深曾拷貝
# 容器 list(串列) tuple(元組) set(集合) dictionary(字典)









