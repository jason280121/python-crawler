
import pandas as pd
import matplotlib.pyplot as plt

# url ='https://stat.taiwan.net.tw/'

plt.rc('font',family='Microsoft Jhenghei')

datas = pd.read_csv('travel.csv')
# print(datas)

total = datas.iloc[1]['亞洲地區']
subtotal = datas.iloc[-1]['小計']
other = int(total) - int(subtotal)


labels = list(datas.columns[2:-1])
labels.append('其他')

data = list(datas.iloc[1][2:-1])
data.append(other)

print(labels)



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

