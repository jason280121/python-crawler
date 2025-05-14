
#物件導向程式 10:27

class Car:
    def __init__(self):
        self.color = 'red'
        self.brand='Tesla'
        self.door = 4


    #定義方法
    def run(self):
        pass



c1 = Car()

# print(c1)
# print(c1.color)
# print(c1.brand)
# print(c1.door)
# print(c1.__dict__)


c2 = Car()
c2.color = 'white'
c2.brand = 'Toyota'
c2.door =5

# print(c2)
print(c2.color)
print(c2.brand)
print(c2.door)
print(c2.__dict__)

