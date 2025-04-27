

# 建立購物選單
menu = {
    'apple': 10,
    'banana': 100,
    'kiwi': 60
}
# 使用迴圈讀取
# apple , banana ,kiwi
# for item in menu:
#     print(item)

# 建立空的list[ ],存放user input key in dict desplay key value
cart = []
total = 0
# print("--------------menu----------------------")
# dict 取出鍵keys : 值values ，顯示目前dict中建立的keys:values
# for k, v in menu.items():
#     print(f'{k:8}:{v:5}')
# print("----------------------------------")

# 撰寫while迴圈，輸入q/Q離開
# while True 會一直執行，不中斷, lower()改成小寫
# ['apple', 'banana', 'kiwi']
while True:
    selected = input("請輸入品項(按q/Q完成輸入:)").lower()
    if selected == 'q':
        break
    # 輸入資料不是None(空值)
    # menu.get(selected) 取得輸入的keys
    elif menu.get(selected) is not None:
        cart.append(selected)

# cart 顯示剛才輸入selected 的keys
# print(cart)


print("訂單內容:")

# 讀取輸入的keys 對應values (訂單內容)
for p in cart:
    # 顯示輸入的keys
    # print(p)
    # get(p)取值，輸入keys, 顯示value
    # print(menu.get(p))

    # get取值(放key)
    # total = total + menu.get(p)
    total += menu.get(p)
# 顯示values 加總
print(total)

print("")  # 空一行
print(f'您一共花費${total}元')
