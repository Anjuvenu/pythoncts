class Student:  # base class or parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name is {self.name} age is {sef.age}")


class Student1(Student):  # clid class oe dup class
    def __init__(self, name, age, std):
        # to access parent class in child calss
        #Student.__init__(self, name, age)  # or
        super().__init__( name, age)
        self.std = std

    def display(self):
        Student.display(self)
        print(f"Standard is {self.std}")


# Then class the child class and we can also acces parent class by this method
name1 = input("Enter name")
age1 = input("Enter age")
std1 = input("Enter standard")
st1 = Student1(name1, age1, std1)
st1.display()
