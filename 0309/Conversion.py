
menory  = float(input("請輸入金額:"))


ext = 0.22

ch  = str(input("日幣轉台幣請輸入jp，台幣轉日幣請輸入nt:"))

if ch == 'jp':
    result = round(menory * exc,0)
    print(f'日幣{ch}約為{result}台幣')
elif ch == 'nt':
    result = round(menory * exc,0)
    print(f'日幣{ch}約為{result}台幣')
else:
    print("不能轉換")

