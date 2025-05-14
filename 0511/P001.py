import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font',family='Microsoft Jhenghei')
datas = pd.read_csv('outbound.csv')
# datas = pd.read_csv('../0504/outbound.csv')

# x = ['A','B','C','D','E']
# h = [30,10,40,50,20]
#
# plt.bar(x,h)
# plt.show()

#讀取所有資料
# print(datas.head())

#有年別，未去除
# print(datas.columns[1:-1])
# print(datas)

#[2:-1] 去除年別
x = datas.columns[2:-1]
h = [int(h) for h in datas.iloc[1][2:-1]]


#測試
# h = datas.iloc[1][2:-1]
# print(type(h))
# print(datas.iloc[1][2:-1])


plt.bar(x,h)
# plt.show()