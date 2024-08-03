class Car:
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color

    def start(self):
        print(self.name ,"Engine started")

car1=Car("toyota",6700000,"white")
car2=Car("swift",5000000,"blue")

print(car2.name,car2.price,car2.color)
print(car2.__dict__)
# print(car1.name,car1.price,car1.color)
# print(car1.__dict__)

car1.start()
car2.start()
