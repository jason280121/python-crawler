# function重覆使用功能，使用函式
# 函式: 功能重覆性，使用函式處理

# 定義函式，直接print
# def foo():
#     x = 100
#     y = 1.2
#     print(x * y)
#     result = x * y
#     print(result)


# 呼叫函式call foo()
# foo()

# 帶參數(一)
# 函式帶入參數值，不需回傳直接print
# 如seting功能設定，只顯示結果，不需回傳值
# def area_p(w, h):
# print(w * h)
# result = w * h
# print(result)


# 呼叫函式call area()
# area(100, 2)


# 帶參數(二)
# 函式帶入參數值，需回傳return
# 結果回傳給原來呼叫者使用。

# def area_r(w, h):
# result = w * h
# return result
# return w * h


# call menthon no1
# result_num = area_r(10, 20)
# print(result_num)


# call methon no2
# # print(area_r(5, 10))


# Default Arguments
# 匯率轉換
# dollar 日幣
# rate 匯率
# dollar :不帶預設值參數要放在(最前面)
# rate=0.22 :帶預設值參數要放在(後面)


import time


def jp_to_tw(dollar, rate=0.22):
    return dollar * rate


# 不帶預設值引數，要放最前面
# 帶預設值引數，要放在不帶預設值引數(後面)
# 如有預設值參數，呼叫時，引數直接使用預設值參數即可，或自行帶入新的引數值

# print(jp_to_tw(10000))
# print(jp_to_tw(10000, 0.23))


# 計時器一 ，從0-4 數字
# 0 1 2 3 4
# def count(start, end):
#     for x in range(start, end):
#         print(x, end=' ')

# count(0, 5)

# 計數器二 ，從0-9 數字, start=0，預設值參數
# 0 1 2 3 4 5 6 7 8 9
# for loop 沒有第三參數，start 起始參數要放前面
# def count(end, start=0):
#     for x in range(start, end):
#         print(x, end=' ')

# count(0, 5)
# count(10)

# 計數器三 ，從0-9 數字, start=0，預設值參數，for loop 加第三參數
# 10 9 8 7 6 5 4 3 2 1
# 因 for loop x有加第三參數，end 可以寫在前面
# def count(end, start=0):
#     for x in range(end, start, -1):
#         print(x, end=' ')

# count(10)


# 計數器四，加入計數延遲與使用者輸入數值
# s = int(input('請輸入數值:'))
# def count(end, start=0):
#     for x in range(end, start, -1):
#         print(x)
#         time.sleep(1)
#     print("完成計數")

# count(s)


# 位置參數1(positional parameter)
# def greeting(first , last):
#     print(f'Hello, {first} {last}')

# greeting('Max' , 'Lee')
# 位置引數(positional argument)，直接帶入預設值
# greeting(last='Tsou', first ='Jason')


# 位置參數2(positional parameter)
# Hello : Tsou Amy
# def greeting(first, last):
#     print(f'Hello : {first}{last}')

# greeting(first='Tsou', last=' Amy')


# 帶入無數引數
# 無限存資料才會使用
# ()
# <class 'tuple' >
# def foo(*args):

    # print(args)
    # print(type(args))
    # for item in args:
    #     print(item, end=' ')
    #     print(type(item))


# foo()
# foo(1, 2, 3, 'Hello', 3.14156, True)


# **kwargs 為<class 'dict' >
# 測試一: 函式定義參數為dict字典型態
# def koo1(**kwargs):
#     print(kwargs)
#     print(type(kwargs))


# koo1()


# **kwargs foo2(**kwargs):
# 測試二: kwargs.items() ，因item 接收後為tuple()型態
# def koo2(**kwargs):
#     for item in kwargs.items():
#         print(item, end=' ')
#         print(type(item))


# koo2(name="Tim", mail='asdf@gmail.com', age=19)


# 測試三: kwargs.tiems() ,f-string keys,values
# name: Jason
# mail: jason58.tsou@gmailcom
# age: 47
# def koo3(**kwargs):
#     for k1, v1 in kwargs.items():
#         print(f'{k1}{v1}')


# koo3(name=': Jason', mail=': jason58.tsou@gmailcom ', age=' : '+str(47))


# 測試不帶預設值引數，位置引數
# ans: 2 3 (7, 8, 9)
# def koo4(x, y, *args):
#     print(x, y, args)


# koo4(2, 3, 7, 8, 9)


# 測試不帶預設值引數，位置引數，關鍵字引數1
# ans:100 200 (33, 44, 55, 66) {'name': 'jason', 'm': 3.14156, 'age': 47}
# def koo5(x, y, *args, **kwargs):
    # print(x, y, args, kwargs)


# koo5(100, 200, 33, 44, 55, 66, name='jason', m=3.14156, age=47)


# 測試不帶預設值引數，位置引數，關鍵字引數2
# ans: 100 80 (999, 888) {'n': 10, 'name': 'test'}
# def koo5(x, y, *args, **kwargs):
    # print(x, y, args, kwargs)


# koo5(100, 80, 999, 888, n=10, name='test')


# 測試不帶預設值引數，位置引數，關鍵字引數3
# ans:
# 100, 80
# [999, 888]
# {'n': 10, 'name': 'test'}
# <class 'list' >
# <class 'dict' >
def koo6(x, y, *args, **kwargs):
    print(x, ',', y)
    result = list(args)
    print(result)
    print(kwargs)
    print(type(result))
    print(type(kwargs))


koo6(100, 80, 999, 888, n=10, name='test')
