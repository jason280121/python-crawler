

import requests
import openpyxl
import bs4

wb = openpyxl.Workbook()
ws = wb.active

# title = ['行程名稱', '顯示價格']
title = ['行程名稱', '顯示價格', '真正價格']


ws.append(title)


for i in range(5):

    url = 'https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&start=0&count=10&destination=D-JP-3256&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=4a69e83e67443471092205ea35b5234d&page='

    # str(i+1) 因為是數字需轉為字串
    url = url + str(i + 1)

    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
        'Cookie': 'CID=7725; UD1=EM; UD2=brand; UD3=sa; UD4=tw; UD5=20734349279; country_lang=zh-tw; currency=TWD; ADID=10101002; KKUD=2d4e493daa285443c273f86737b8a862; _gcl_au=1.1.77692454.1744632995; _ga=GA1.1.469921019.1744632997; _fbp=fb.1.1744632997351.598754162415603439; rskxRunCookie=0; rCookie=dibaxej36ki19aaug7lzlnm9f3nz6h; CookieConsent={stamp:%274sSQDGPvWAL9cgGDBop3K93/hVoYz4kiM/IQSUCAOK+xbq6Hs+l5AA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1744633000457%2Cregion:%27tw%27}; _hjSessionUser_628088=eyJpZCI6ImFkYWIyYWEzLTA1NWQtNTBmNy04Zjk2LTczNjliMDU4MTA0YSIsImNyZWF0ZWQiOjE3NDQ2MzI5OTczOTUsImV4aXN0aW5nIjp0cnVlfQ==; __lt__cid=527d54fc-6f67-417f-bec7-032534b30acf; _gcl_gs=2.1.k1$i1744679291$u214784013; _gcl_aw=GCL.1744679298.CjwKCAjw5PK_BhBBEiwAL7GTPVJB202hhzpTyi4SZ1dLge8hzitSfNjV_ToxswdJ-HQkUlUo7pIapBoCUgcQAvD_BwE; csrf_cookie_name=4a69e83e67443471092205ea35b5234d; KKWEB=a%3A3%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2298a71877daa2fde4bb0d1e0c04aa2691%22%3Bs%3A7%3A%22channel%22%3Bs%3A6%3A%22GOOGLE%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1744718873%3B%7D090f6288462c81a08a90eb2400f5c038; _hjSession_628088=eyJpZCI6IjBmZDdlZjAxLWJkNDgtNDBjNS05OGU1LTIxOTA4ZWZjODgzMiIsImMiOjE3NDQ3MjY1MTI0NDIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; __lt__sid=866d2447-bc7544a6; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%222d4e493daa285443c273f86737b8a862%22%2C%22expiryDate%22%3A%222026-04-15T14%3A20%3A36.711Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22NZBBX9SZFD3z8XUuGSXR%22%2C%22expiryDate%22%3A%222026-04-15T14%3A20%3A36.711Z%22%7D; _uetsid=b3013720192611f0ab626f81b8e0ec92; _uetvid=71887cd0181911f0a4936bda7701fba5; cto_bundle=atUmBl9USFVlaEhFeHB2dlFsRHN3UU9ORGZQRGNwcVJPMVZPMVp2eTUyaEdRczNOQXZrMEhmdnF2SUkySDduNjFtMXlDOXMwVzI5dHV3blVNR2k4eU5PdCUyQjlSRnhtaDgxak84Q3lTd3FrUCUyRmlHdWNuWHNod0N6czgxVkMlMkZVZEpENEROWEx5TjF3JTJCOWVDYVZaUm51dW5CNEpyUSUzRCUzRA; header_data_updated=1744728085; lastRskxRun=1744728088941; datadome=Y_aWQb2jEmJl06TnrB6lU588p4JC9IaGISuQ0BDNwPpkwIGBMPlRp5uSt46Ds3C2nARR3ov9akGQpTRW~_7ji_C1GN3W_8j8LI_l3WDeIqNkyzJaQ3hGRGRDQfzzJklC; _ga_RJJY5WQFKP=GS1.1.1744726405.6.1.1744728569.56.0.0'
    }

    # 第一種方式，使用requests
    datas = requests.get(url, headers=header, verify=False)
    # print(datas)

# 使用(datas['data'])json方式
    datas = datas.json()
    # print(datas)

    with open('jason_11.xlsx', 'w', encoding='utf-8') as file:
        for data in datas['data']:
            file.write(
                f'{data['name']} : {data['display_price']} :{data['display_sale_price']}')
            item = []
            item.append(data['name'])
            item.append(data['display_price'])
            item.append(data['display_sale_price'])
            ws.append(item)
            # print(item)
wb.save('jason_10.xlsx')
