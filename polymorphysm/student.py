class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print("Hi my name is"+ self.name,"and my age is"+str(self.age))
class Student(Person):
    def __init__(self,name,age,stid):
        super().__init__(name,age)
        self.stid = stid
    def introduce(self):
        super().introduce()
        print(f"and my student id is {self.stid}")
class Teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def introduce(self):
        super().introduce()
        print("and I make"+ str(self.salary),"per year")
student1=Student("John",20,857)
student1.introduce()
teacher1=Teacher("Joseph",40,50000)
teacher1.introduce()
