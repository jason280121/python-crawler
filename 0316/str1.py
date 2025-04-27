

#空格10格
# a = 'Hello %s'
# print(a % 'John')

# a1 = 'Hello %10s'
# a2= 'Hello %-10s'
# a3 = 'Hello %+10s'
# print(a1 % 'John')
# print(a2 % 'John')
# print(a3 % 'John')


#
# b1= 'Hello %d'
# b2= 'Hello %.5d'
# b3= 'Hello %.4d'
# b4= 'Hello %10d'
# print(b1 % 123)
# print(b2 % 123)
# print(b3 % 123)
# print(b4 % 123)

#.3 小數點3位
# c1 = 'Hello %f'
# c2 = 'Hello %.5f'
# c3 = 'Hello %-.9f'
# print(c1 % 3.14156)
# print(c2 % 3.14156)
# print(c3 % 3.14156)

#有多個顯示字串文字
# msg = ' Hello %s ! 今天氣溫為 %.1f 度C'
# print(msg % ('jason',13))

# msg1 = 'Hello %s ! 明天的天氣預測為%.2f 度C'
# print(msg1 % ('jason',37.58))



#format
# : 格式
# s=字串，d=整數，f:浮點數 o=八進位，x=16，b=2進位 , 方向顯示(> < ^)
# 沒有冒號不設定任何格式(型態)都會印出
# msg = 'hello {}'


# msg = 'hello {:^12s}'
# msg = 'hello {:-^12s}'
# msg = 'hello {:-<12s}'
# msg = 'hello {:->12s}'
# print(msg.format('jason'))

# msg1 = 'Hello {:-^8d}'
# msg1 = 'Hello {:->8d}'
# msg1 = 'Hello {:-<8d}'
# print(msg1.format(123))


# msg2 = 'Hello {:@^10.5f}'
# msg2 = 'Hello {:-^12.5f}'
# msg2 = 'Hello {:+^18.5f}'
# print(msg2.format(3.14156))


#顯示位置 0 ,1
# msg = 'hello {0} ! 今天的氣溫為 {1}度C'
# print(msg.format('jason',10))



#顯示位置 1 ,0
# msg = 'Hello {1} ! 今天的氣溫為 {0}度C'
# print(msg.format('jason', 10))


# msg = 'Hello {name} ! 今天的氣溫為 {deg}度C'
# print(msg.format(name = 'jason', deg=100))

# msg = 'hello {deg} ! 今天的氣溫為 {name}度C'
# print(msg.format(name = 'jason', deg=10))


# msg = 'hello {name} ! 今天的氣溫為 {deg:.2f}度C'
# print(msg.format(name = 'jason', deg=10))


# f-string
# name ='John'
# print(f'hello {name}')


# name = 'jason'
# deg =12
# print(f'Hello {name} 今天氣溫為{deg}度C')

# print(f'Hello {name} 今天氣溫為{deg:.1f}度C')

# print(f'Hello {name:-^12s} 今天氣溫為{deg:.1f}度C')
