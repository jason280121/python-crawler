

# 宣告空串列[ ]
# []
# <class 'list' >
# empty_list = []
# print(empty_list)
# print(type(empty_list))


# 宣告空元組tuple()
# ()
# <class 'tuple' >
# empty_tuple = ()
# print(empty_tuple)
# print(type(empty_tuple))

# 宣告空集合set{ }
# set()
# <class 'set' >
# empty_set = set()
# print(empty_set)
# print(type(empty_set))


# 宣告空字典dict{ }
# {}
# <class 'dict' >
# empty_dict = {}
# print(empty_dict)
# print(type(empty_dict))


# dict有屬性的list
'''大數據資料一般使用list為主與dict為輔
    ,下載或者整理完資料後，在使用set移除重覆性，
    最後使用tuple(不能更改資料)[比對]整理後資料'''

# 建立空字典方式
# {}
# <class 'dict' >
# args = {}
# print(args)
# print(type(args))


# dict 鍵 : 值
#      '屬性' : '值'
#      'key':'value'
# {0: 13, 1: 14, 2: 15}
# args = {0: 13, 1: 14, 2: 15}
# print(args)


# 建立dict{ }資料集
# {0: 13, 1: 14, 2: 15}
user = {
    'name': 'jason',
    'email': 'jason58.tsou@gmail.com',
    'gender': 'male',
    'skill': ['photoshop', 'python'],
}
# print(user)


# use get method read dict key name
# print(user.get('name'))
# print(user['name'])


# dict資料集中，沒有的鍵值讀取會產生錯誤
# print(user['skill'])


# 新增dict資料
# 新增skill鍵，增加一筆value，第一種方式
# {'name': 'jason', 'email': 'jason58.tsou@gmail.com',
#     'gender': 'male', 'skill': 'Photoshop'}
# user['skill'] = 'Photoshop'
# print(user)


# skill 增加一筆value，第二種方式
# user.setdefault('skill', 'PhotoShop')

# print(user)

# 讀取skill key
# PhotoShop
# print(user.get('skill'))
# print(user['skill'])


# 使用dict 資料集修改方式
# user['name'] = 'Max'
# print(user)


# 使用setdefault() 方法不能修改dict key value 值
# user.setdefault('name', 'max')
# print(user)

# '鍵' : '值'
# 另建dict資料集
# {'台北市': 15, '桃園市': 15}
# temp = {
#     '台北市': 15,
#     '桃園市': 15,

# }
# print(temp)

# list [ 放dict]  說明
# 第0個資料集
users = [
    {
        'name': 'jason',
        'email': 'jason58.tsou@gmail.com',
        'gender': 'male',
        'skill': ['PhotoShop', 'Python'],

    },
    # 第1個資料集
    {
        'name': 'amy',
        'email': 'amy@gmail.com',
        'gender': 'female',
        'skill': ['PhotoShop', 'Python', 'Html'],
        # 如果skill 鍵值空白要用以下2種方式撰寫
        # 'skill' : []
        # 'skill' : [None]
    }
]

# print(users)

# 讀取list 中的dict 鍵:
# print(users[0]['name'])
# print(users[1]['name'])
# print(users[0]['email'])
# print(users[1]['email'])
# print(users[0]['gender'])
# print(users[1]['gender'])
# print(users[0]['skill'])
# print(users[1]['skill'])


# 讀取第0個list元素中，skill第N個value
# PhotoShop, Python
# print(users[0]['skill'][0])
# print(users[0]['skill'][1])


# 讀取第1個list元素中，skill第N個value
# PhotoShop, Python, Html
# print(users[1]['skill'][0])
# print(users[1]['skill'][1])
# print(users[1]['skill'][2])

# dict 使用pop()刪除
# {'name': 'jason', 'email': 'jason58.tsou@gmail.com',
#     'skill': ['photoshop', 'python']}
# del user['gender']
# print(user)


# clear() 清空
# {}
# user.clear()
# print(user)

# 讀取、鍵key
# dict_keys(['name', 'email', 'gender', 'skill'])
# print(user.keys())


# 讀取，值value
# dict_values(['jason', 'jason58.tsou@gmail.com',
#             'male', ['photoshop', 'python']])
# print(user.values())

# 讀取全部 (鍵:值) key: value
# dict_items([('name', 'jason'), ('email', 'jason58.tsou@gmail.com'),
#            ('gender', 'male'), ('skill', ['photoshop', 'python'])])
# print(user.items())


# 字典dict 個別取值較麻煩(以下)，需用迴圈方式取值
# print(users[0]['name'])
# print(users[1]['name'])
# print(users[0]['email'])
# print(users[1]['email'])
# print(users[0]['gender'])
# print(users[1]['gender'])
# print(users[0]['gender'])
# print(users[1]['gender'])


# for in 取(鍵) , 讀取user dict 資料集
# name,email,gender,skill
# for item in user.keys():
#     print(item)


# name,email,gender,skill
# for item1 in user:
#     print(item1)


# for in 取(值) , 讀取user dict 資料集
# jason ,jason58.tsou@gmail.com,
# male ,['photoshop', 'python']
# for v1 in user.values():
#     print(v1)

# for in 取(鍵:值) , 讀取user dict 資料集
# ()'name', 'jason'),('email', 'jason58.tsou@gmail.com'),
# ('gender', 'male'),('skill', ['photoshop', 'python'])
# for item in user.items():
#     print(item)

# for in 取(鍵:值),帶2個參數，讀取user dict 資料集
# for key, val in user.items():
#     print(key, val)
#     print(f'{key:10}:{val}')
# val:10 不能設定，因為list[]中有值


# (第一次)自己撰寫的list[] 雙迴圈，讀dict
# for k1, v1 in users[0].items():
#     print(f'{k1:10}:{v1}')
# print("--------第二個list[] dict --------------------------")
# for k2, v2 in users[1].items():
#     print(f'{k2:10}:{v2}')

# (第二次)自己撰寫的list[] 雙迴圈，讀dict
# for key1 in range(len(users)):
#     for k1, v1 in users[key1].items():
#         print(f'{k1:10}:{v1}')
#     print("------------------------------------------------------")

# 字典與字典的結合,使用update()
# 更新、新增鍵:值(第一種方式)
# 新增dict user2{'age' : 30 }與更新'name' : 'jeremy'
'''dict user 有的值如'name': 'jason', 
use user2時會更新覆蓋:name(鍵) '''
# 'name': 'jeremy', 'age': 30
user2 = {
    'name': 'jeremy',
    'age': 30,
}
# print(user)
# user.update(user2)
# print(user)
# 新增dict user3={'active': 'True'}
user3 = {
    'active': True
}

# 更新、新增鍵:值(第二種方式)
# 新增user2(鍵:值)到user
# user = {**user, ** user2}
# print(user2)
# print("------------------------------")
# print(user)

# 新增user2 , user3(鍵:值)到user
# 更新 'name': 'jeremy', 'age': 30, 'active': True
# user = {**user, **user2, **user3}
# print(user2)
# print("------------------------------")
# print(user3)
# print("------------------------------")
# print(user)


# 不確定能使用，需外掛
# user.update(user2).update(user3)


# user2 更新資料到user
# user.update(user2)
# print(user2)
# print(user)
