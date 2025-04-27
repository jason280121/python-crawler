m = input("oz轉ml請輸入1，ml轉oz請輸入2:")
exc = 29.573
if m =='1':
    d= float(input('請輸入oz重量:'))
    # result = d *exc

    result = round(d * exc,3)
    # result= round(result, 0)
    print(f'oz{d}約為{result}ml')


else:
    d = float(input('請輸入ml重量:'))
    # result = d / exc
    result = round(d / exc,3)
    # result= round(result, 0)
    print(f'ml{d}約為{result}oz')