class Student_Details:
    def __init__(self, name, age):
        self.name_of_student = name
        self.age_of_student = age


    def display(self):
        print(f"Student name is {self.name_of_student} and his/her age is {self.age_of_student}")

Student_name=input("Enter your name")
Student_age=input("Enter your age")
Student_1 = Student_Details(Student_name,Student_age)
Student_1.display()
