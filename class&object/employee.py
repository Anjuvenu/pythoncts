class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def employee(self):
        print(self.name,20000)
employee1=Employee(102,"Anju",20000)
employee2=Employee(105,"Rohini",20000)

print(employee1.id,employee1.name,employee1.salary)
print(employee2.id,employee2.name,employee2.salary)

  


        