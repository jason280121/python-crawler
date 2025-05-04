import twstock

#安裝套件
# pip install twstock
# pip install lxml

#取得一週指數
#取得開盤、收盤，交易量
#台積電
# result = twstock.Stock('2330')
result = twstock.Stock('3037')

#其它股票資訊
# result = twstock.codes('3037')
print(result)

