
#物件導向程式 10:27

class Car:
    def __init__(self,color,brand,door):
        self.color = color
        self.brand= brand
        self.door = door


    #定義方法，方法內顯示屬性內容
    def run(self):
        print(f'您的車品牌是{self.brand}, 顏色為:{self.color}, 車門:{self.door}')

# c1 = Car()
c1 = Car('red','Tesla',4)
c1.run()


# c2 = Car()
c2 = Car('white','Toyota',5)
c2.run()


