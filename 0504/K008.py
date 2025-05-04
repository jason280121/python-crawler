
# import pandas as pd
import matplotlib.pyplot as plt



#設定顯示字體
#正黑體
plt.rc('font',family ='Microsoft Jhenghei')

datas = [22,55,88]



# labels=['A','B','C']
labels=['初階','中階','高階']
color= ['purple','blue','yellow']

#圓餅圖
# plt.pie([10,20,30])


plt.pie(datas,
        labels=labels,
        #radius 比例
        radius=1,

        #圖標距離(外觀) 0.5
        labeldistance=1.2,

        #文字屬性, 文字大小,normal是預設值、bold是粗體
        textprops={'size':16,
        'weight':'bold'},

        #百份比
        autopct='%.2f%%',
        colors=color


        )

plt.legend()

plt.show()
