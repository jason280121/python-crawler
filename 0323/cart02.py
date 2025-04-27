

menu = [
    {
        'id': 1,
        'name': '1.滷肉飯',
        'price': 50,

    },
    {
        'id': 2,
        'name': '2.牛肉麵',
        'price': 120,

    },
    {
        'id': 3,
        'name': '3.貢肉湯',
        'price': 40,

    },
]

cart = []
total = 0

print("-----------------menu--------------")
for item in menu:
    # 讀取menu key : value 值
    # print(item['name'], item['price'])
    print(f'{item['name']}:{item['price']}')
print("-----------------------------------")

print("")

while True:
    selected = input('請輸入品項編號(按q/Q完成輸入):').lower()
    if selected == 'q':
        break
    elif int(selected) > len(menu):
        continue
    elif menu[int(selected) - 1] in menu:
        cart.append(menu[int(selected) - 1])
# print(cart)

for item in cart:
    print(item['name'])
    total += item['price']

print(total)
