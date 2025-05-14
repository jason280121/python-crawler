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
    pass

#繼承Car類別
class Tesla(Car):
    pass


t1= Toyota('write',5)
print(t1.__dict__)
t1.run()

t2 = Tesla('red',4)
print(t2.__dict__)
t2.run()