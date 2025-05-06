import matplotlib.pyplot as plt

listx = [16, 26, 38, 15, 22, 30]
listy = [1, 3, 5, 7, 9, 11]

#設定顯示字體
#正黑體
plt.rc('font',family ='Microsoft Jhenghei')
#新明細體
# plt.rc('font',family ='Microsoft PMingLiU')
# 標楷體
# plt.rc('font',family ='Microsoft DFKai-SB')


plt.plot(listx,listy, marker='s', color='#ff8c00', linestyle='-',linewidth=1,markersize=10,label='may')
#語言

#標題
plt.title('test')

#日(X軸)
plt.xlabel('day')

#氣溫(y軸)
plt.ylabel('degree')


#坐標範圍
plt.xlim(1,7)
plt.ylim(1,50)

# x= [1,2,3,4,5,7,8,9,10]
# y= [1,2,3,4,5,7,8,9,10]

#刻度
plt.xticks(range(1,10,2))
plt.yticks(range(1,51,3))


#圖例說明
plt.legend()



#自己照網頁增加
plt.tick_params(
    #針對哪個軸做設定，預設 both，可以設定 x 或 y。
    axis = 'x',
    #刻度顏色
    color ='red',
    # 刻度和刻度文字的顏色。
    colors ='green',
    #刻度寬度
    width= 5,
    #刻度長度
    length=10,
    #刻度位置，預設 out，可以設定 in 或 inout。
    direction='inout'

)


plt.show()
