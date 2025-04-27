
import  matplotlib.pyplot as plt
import numpy as np




# listx_x = [1,2,3,4,5]
# plt.plot(listx_x)
# plt.show()

listx_x = [16,26,38,15,22,30]
listx_y = [1,3,5,7,9,11]

# plt.plot(listx_x,listx_y)
plt.plot(listx_x,listx_y, marker='s', color='#f5deb3', linestyle='-',linewidth=1,markersize=10)

#marker 標記
# o * . v s


#顏色
#-, -
#linewidth 設定線條寬度
#markersize=20   標記大小



#抬頭
plt.title('test shape')


#設定圖例名稱
#x 軸
plt.xlabel('degree')


#y 軸
plt.ylabel('day')

plt.show()







