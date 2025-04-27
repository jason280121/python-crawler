

# 帶入無限引數
# 無限存資料才會使用
# *args 為 tuple()型態
# def foo (*args):
# 空的tuple() 型態
# print(args)
# print(type(args))

# for item in args:
#     print(item, end=' ')

# foo()
# foo(1,2,3,4,'Hello')


# **kwargs dict{ }型態
def foo2(**kwargs):
    #     print(kwargs)
    #     print(type(kwargs))
    #
    # foo2()

    for item in kwargs.items():
        print(item, end=',')
        # print(type(item))


foo2(name=":Tim ", mail=':jason58.tsou@gmail.com', age=19)


# use for loop read kwargs,items(),keys,values
#     for k,v in kwargs.items():
#         print(f'{k}{v}')
# foo2(name=":Tim ", mail=':jason58.tsou@gmail.com', age=19)


# 測試不帶參數引數，位置引數，關鍵字引數
# def foo3(x , y , *args):
# def foo3(x, y, *args, **kwargs):
#     print(x, y ,args,kwargs)
#
# foo3(100, 80, 999,888, n=10 ,name='test')
