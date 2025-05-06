
import pandas as pd

#openpyxl

#下載csv檔
datas = pd.read_csv('Restaurant_C_f.csv')
# datas = pd.read_csv('Restaurant_C_f.csv',encoding='utf-8')
# datas = pd.read_csv('Restaurant_C_f.csv',encoding='big5')
# print(datas)

# print(datas.columns)
# print(datas['Name'])
# print(datas['Add'])




# 11:45
#大五碼
#encoding = 'big5'

#抓中壢資料
condition = datas['Add'].str.contains('中壢')
result = datas[condition]
# print(result)
# print(result['Add'])
# print(result['Name'])

#只存三個欄位
# result =result[['Name','Add','Tel']]

#刪欄位資料
result =result.drop(['Id','Px','Py'], axis=1)

#刪欄資料
# result =result.drop(['Id','Px','Py'], axis=0)


#儲存全部
result.to_excel('chungli.xlsx')










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


#12:15

