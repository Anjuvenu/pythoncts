class Car:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def start(self):
        print(f"{self.name} started")


car1 = Car("Toyota", 2000000, "Blue")
car2 =Car("maruti",3000000,"white")
#change
car1.price=400000

car2.color="red"

#delete
# del car1.color

print(car1.name,car1.price,car1.color)
print(car2.name,car2.price,car2.color)

car1.start()
car2.start()

