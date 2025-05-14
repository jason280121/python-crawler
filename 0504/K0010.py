
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font',family='Microsoft Jhenghei')

pets = pd.read_csv('COA_OpenData.csv')

# animal_kind(動物的類型)、animal_Variety(動物品種)
# print(pets)

#全部筆數
total = pets['animal_id'].count()
# print(total)


#貓
cats = pets[pets['animal_kind'].str.contains('貓')]
cats_total = cats['animal_id'].count()
# print(cats_total)
#狗
dogs = pets[pets['animal_kind'].str.contains('狗')]
dogs_total = dogs['animal_id'].count()
# print(dogs_total)

#其它
other  = pets[pets['animal_kind'].str.contains('貓|狗')== False]
other_total = total - cats_total - dogs_total

#動物的類型
print(other['animal_kind'])

#動物品種
# print(other['animal_Variety'])

#讀取全部
result =cats[['animal_id','animal_kind','animal_Variety']]

#讀取全部
# result=pets[['animal_id','animal_kind','animal_Variety']]


plt.pie([dogs_total, cats_total, other_total],
        labels=['狗','貓','其他'],
        autopct='%.1f%%',
        explode=[.1, .1, .5]
        )




plt.legend()
# plt.show()

# result.to_excel('animal.xlsx')