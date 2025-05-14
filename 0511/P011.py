#父類別
class Car:
    def __init__(self,color,door):
        self.color = color
        self.door = door

    #建立類別method
    def run(self):
        print(f'你的車顏色為{self.color}')

#繼承Car類別
class Toyota(Car):
    # pass
    # brand = 'Toyota'
    # def __init__(self, color, door,brand):
    def __init__(self, color, door):
        super().__init__(color, door)
        # self.brand = brand
        self.brand = 'Toyota'



#繼承Car類別
class Tesla(Car):
    # def __init__(self, color, door,brand):
    def __init__(self, color, door):
        super().__init__(color, door)
        # self.brand = brand
        self.brand = 'Tesle'

# t1= Toyota('write',5,'toyota')
t1= Toyota('write',5)
print(t1.__dict__)
print(t1.brand)
# t1.run()

# t2 = Tesla('red',4,'Tesla')
t2 = Tesla('red',4)

print(t2.__dict__)
print(t2.brand)
# t2.run()