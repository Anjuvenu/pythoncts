class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def indroduce(self):
        print(f"My name is {self.name} and my age is {self.age}")
class student(Person):
    def __init__(self,name,age,studentid):
        super().__init__(name,age)
        self.studentid=studentid
    def indroduce(self):
        super().indroduce()
        print("My student id is"+str(self.studentid))
class teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def indroduce(self):
        super().indroduce()
        print("and my salary is "+self.salary)
student1=student("akshay","22","1234")
teacher1=teacher("rohini","33","23456780")
student1.indroduce()
teacher1.indroduce()