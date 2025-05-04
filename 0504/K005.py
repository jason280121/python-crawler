
import pandas as pd

#安裝套件
#pip install pandas



#10:50
data3 = pd.DataFrame(
    {
        'name':['Zac','Andy','Tim'],
        'age':[30,32,28]
    },
    # index=['A','B','C']
)
# print(data3)

#size 欄位釋量
# print(data3.size)

#shape 形狀
# print(data3.shape)

#columns 行
# print(data3.columns)

#index  列
# print(data3.index)



# 三列二行
# print(data3['name'])
# print(data3['age'])
# print(data3.iloc[0])
# print(data3.loc[1])
# print(data3.loc['C'])


data4 = pd.DataFrame(
    [
        {'name':'Zac','age':32},
        {'name':'Max','age':28},
        {'name':'Andy','age':30}
    ]
)


# print(data4)


# print(data4.size)
# print(data4.shape)
# print(data4.columns)
# print(data4.index)
# print(data4.iloc[1])
# print(data4.loc[2])

#11:19