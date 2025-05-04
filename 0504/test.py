import matplotlib.pyplot as plt

listx = [16, 26, 38, 15, 22, 30]
listy = [1, 3, 5, 7, 9, 11]

plt.plot(listx,listy, marker='s', color='#ff8c00', linestyle='-',linewidth=1,markersize=20)
plt.title('test')
plt.xlabel('degree')
plt.ylabel('day')

plt.show()


# pip install twstock
# pip install lxml