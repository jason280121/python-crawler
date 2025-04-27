import requests

# 連續存 10頁，&page=1，字串移至url 網址最末端
for i in range(10):
    url = 'https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=e62adcc7d7bd0ecbe5e1fed2da03a4f8&page='

    # str(i+1) 因為是數字需轉為字串
    url = url + str(i + 1)

    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
        'Cookie': 'csrf_cookie_name=e62adcc7d7bd0ecbe5e1fed2da03a4f8; KKWEB=a%3A4%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22107a1d3433f2dbb0b6e5eafdef315d5c%22%3Bs%3A7%3A%22channel%22%3Bs%3A5%3A%22GUEST%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1744515789%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D191c5ff7960f5750643884127ce0bb78; CID=7725; UD1=EM; UD2=brand; UD3=sa; UD4=tw; UD5=20734349279; country_lang=zh-tw; currency=TWD; ADID=10101002; KKUD=107a1d3433f2dbb0b6e5eafdef315d5c; _gcl_gs=2.1.k1$i1744515788$u214784013; _gcl_au=1.1.1772200333.1744515797; _ga=GA1.1.287201269.1744515797; _fbp=fb.1.1744515797865.852615746141844053; __lt__cid=527d54fc-6f67-417f-bec7-032534b30acf; __lt__sid=866d2447-f0c6fe62; _hjSession_628088=eyJpZCI6IjE0MTViMTc1LTI1ZmQtNGNhMi1hMmViLTQ3OWMyY2MyY2U0MSIsImMiOjE3NDQ1MTU3OTc5NjYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; rskxRunCookie=0; rCookie=dibaxej36ki19aaug7lzlnm9f3nz6h; _hjSessionUser_628088=eyJpZCI6ImJiMDljODMxLTQxOTktNTFlYi1iNmIzLTg3NjQ4ZTBiMjdmOSIsImNyZWF0ZWQiOjE3NDQ1MTU3OTc5NjUsImV4aXN0aW5nIjp0cnVlfQ==; CookieConsent={stamp:%27Akq1m5UUNeVSdCniFc+2AwtQVYTuU/KGItQf2GzgTuSYEwK2li2JDA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1744515819294%2Cregion:%27tw%27}; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22107a1d3433f2dbb0b6e5eafdef315d5c%22%2C%22expiryDate%22%3A%222026-04-13T04%3A21%3A04.426Z%22%7D; lastRskxRun=1744518095050; cto_bundle=R_ahGF9USFVlaEhFeHB2dlFsRHN3UU9ORGZFeU10ZDF0NVFNSmFmanNocUxwTzdEc2diZlhXYlE5VFBOalpwbmlDQUpaSXNuWmxuRTlWc1dzOUc5S2pMazNpV2J0MHduamFMOSUyRjBsQSUyRks4R3pSN2tvSXh5cUVCNkhTZkl1SFMzekVFVnNLTlJOZ3VRWXhJVTIwZjBZUVl6MjBBJTNEJTNE; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22NZBBX9SZFD3z8XUuGSXR%22%2C%22expiryDate%22%3A%222026-04-13T04%3A22%3A05.718Z%22%7D; _uetsid=71883c80181911f0bf661b32a129dd3a; _uetvid=71887cd0181911f0a4936bda7701fba5; datadome=8hDucszzyD42LWlAgUoqHONBxNH1D8RN3jj57WIvaz1ujE5T9AoNeK8DN2OxaasPd~y7paPBjI8a7BHAjXTKWve9cFIGQJGeyvanKx50Nqu1zA73472vJH3BTA3~cjLd; _ga_RJJY5WQFKP=GS1.1.1744515796.1.1.1744518189.60.0.0; _gcl_aw=GCL.1744518200.Cj0KCQjwnui_BhDlARIsAEo9GuviRI4lazPTopBpaemNprRQY6wkFjc2XgeZa9JELKrzXYMYrLaoDhsaAjh5EALw_wcB'
    }

    # requests 讀入Header與verify=False
    datas = requests.get(url, headers=header, verify=False)

    # 使用json()模式
    # (datas['data'])
    datas = datas.json()

    # 'w' 只寫一頁，連續存寫頁面要用'a'
    with open('kkday_excel_02.xlsx', 'a', encoding='utf-8') as file:
        for data in datas['data']:
            file.write(f'{data['name']} : {data['price']}\n')
