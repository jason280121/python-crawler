
#物件導向程式 10:27

class Car:
    def __init__(self,color,brand,door):
        self.color = color
        self.brand=brand
        self.door = door

    def run(self):
        pass


# c1 = Car()
c1 = Car('red','Tesla',4)
#c1物件定義屬性
# c1.color = 'red'
# c1.brand = 'Tesla'
# c1.door =4
# print(c1)
print(c1.color)
print(c1.brand)
print(c1.door)
print(c1.__dict__)


# c2 = Car()
c2 = Car('white','Toyota',5)
#c2物件定義屬性
# c2.color = 'white'
# c2.brand = 'Toyota'
# c2.door =5

# print(c2)
print(c2.color)
print(c2.brand)
print(c2.door)
print(c2.__dict__)

