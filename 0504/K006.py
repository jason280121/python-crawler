
import pandas as pd

#下載csv檔
datas = pd.read_csv('Restaurant_C_f.csv')
# print(datas)

# print(datas.columns)
# print(datas['Name'])
# print(datas['Add'])
# print(f'{datas['Name']}:{datas['Add']}')




#抓中壢資料
condition = datas['Add'].str.contains('中壢')
result = datas[condition]
# print(result)
# print(result['Add'])
# print(result['Name'])

# for data in result:
#     print(f'{data['Name']}:{data['Add']}')




#政府資料開放平臺
#動物
#動物認領養  下載csv

# datas = pd.read_csv('COA_OpenData.csv')
# print(datas.columns)
# print(datas['animal_kind'])
# condition = datas['animal_kind'].str.contains('貓')
result = datas[condition]
# print(result)

# print(datas['animal_Variety'])


