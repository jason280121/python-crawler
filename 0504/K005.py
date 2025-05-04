
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
        {'name': 'Zac', 'age': 32, 'gender': 'M'},
        {'name': 'Max', 'age': 28, 'gender': 'M'},
        {'name': 'Andy', 'age': 30, 'gender': 'M'},
        {'name': 'Amy', 'age': 22, 'gender': 'F'},
        {'name': 'Laura', 'age': 26, 'gender': 'F'}
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






#最大值
# print(data4['age'].max())

#最小值
# print(data4['age'].min())

#平均值
# print(data4['age'].mean())

#標準差
# print(data4['age'].std())

#顯示1 age
# condition  = data4['age'] > 30
# print(data4[condition])

#顯示2 age
# print(data4[data4['age'] > 30])


#顯示3 gender
# condtition  = data4['gender'].str.contains('F')
print(data4[condtition])

#顯示3 gender
# print(data4[data4['gender'].str.contains('M')])

