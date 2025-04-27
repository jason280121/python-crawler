
m = input("日幣轉台幣請輸入1，台幣轉日幣請輸入2:")
exc = 0.2198
if m =='1':
    d= float(input('請輸入日幣金額:'))
    # result = d *exc

    result = round(d * exc,0)
    # result= round(result, 0)
    print(f'日幣{d}約為{result}台幣')


else:
    d = float(input('請輸入台幣金額:'))
    # result = d / exc
    result = round(d / exc,0)
    # result= round(result, 0)
    print(f'台幣{d}約為{result}日幣')