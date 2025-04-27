import requests

# import ssl



# url ='https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=9b651a1b-0732-418e-b4e9-e784417cadef&limit=1000&sort=ImportDate%20desc&format=JSON'

#AQI
url ='https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=9b651a1b-0732-418e-b4e9-e784417cadef&limit=1000&sort=ImportDate%20desc&format=JSON'


#YOUBIKE
# url ='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'


results = requests.get(url,verify=False)

# print(results)
# print(results.text)

results = results.json()
for results in results['records']:
    print(f'{results['sitename']}:AQI{results['aqi']}')



#you bike
# for  result in results:
#     print(f'{result['sna']}:可租借車輛{result['available_rent_bikes']}')


