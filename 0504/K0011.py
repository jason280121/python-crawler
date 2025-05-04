
import pandas as pd
import matplotlib.pyplot as plt

# url ='https://stat.taiwan.net.tw/'

plt.rc('font',family='Microsoft Jhenghei')

datas = pd.read_csv('travel.csv')
# print(datas)

labels = datas.columns[2:-1]
# print(labels)

data = datas.iloc[1][2:-1]
# print(data)

plt.pie(data,
        labels=labels,
        #radius 比例
        radius=1,

        #圖標距離(外觀) 0.5
        labeldistance=1.2,

        #文字屬性, 文字大小,normal是預設值、bold是粗體
        textprops={'size':12,
        'weight':'bold'},

        #百份比
        autopct='%.2f%%'

        )

plt.legend()
plt.show()

