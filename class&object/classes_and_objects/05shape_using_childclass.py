import math


class shape:
    def __init__(self):
        pass

        def calculate_area(self):
            pass

        def calculate_perimeter(self):
            pass


#   Shape circle
class circle(shape):
    def __init__(self):
        self.perimeter = None
        self.area = None
        self.radius = int(input("Enter the radius:"))

    def calculate_area(self):
        self.area = math.pi * self.radius ** 2
        print(f"The area of the circle with radius {self.radius} = {self.area} ")

    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        print(f"The perimetr of the circle with radius {self.radius} = {self.perimeter} ")


# 2 Shape rectangle
class rectangle(shape):
    def __init__(self):
        self.perimeter = None
        self.area = None
        self.height = int(input("Enter the height:"))
        self.width = int(input("Enter the width:"))

    def calculate_area(self):
        self.area = self.height * self.width
        print(f"The area of the circle with height {self.height} and {self.width}= {self.area} ")

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.height + self.width)
        print(f"The perimeter of the circle with height {self.height} and {self.width}= {self.perimeter} ")


# Shape triangle
class triangle(shape):
    def __init__(self):
        self.perimeter = None
        self.area = None
        self.height = int(input("Enter the height:"))
        self.base = int(input("Enter the length of base:"))
        self.side2 = int(input("Enter the length of side 1:"))
        self.side3 = int(input("Enter the length of side 2:"))

    def calculate_area(self):
        self.area = (self.base * self.height) / 2
        print(f"The area of the triangle with height {self.height} and base length {self.base}= {self.area} ")

    def calculate_perimeter(self):
        self.perimeter = self.base + self.side2 + self.side3
        print(f"The perimeter of the circle with side {self.base} , {self.side2} and {self.side3}= {self.perimeter} ")


choose_shape = int(input("Press 1 for circle,Press 2 for rectangle, Press 3 for triangle:"))
if choose_shape == 1:
    circle_cal = circle()
    operation = int(input("Press 1 for calculate area,Press 2 for calculate perimeter or Press 3 for both:"))
    if operation == 1:
        circle_cal.calculate_area()
    elif operation == 2:
        circle_cal.calculate_perimeter()
    elif operation == 3:
        circle_cal.calculate_area()
        circle_cal.calculate_perimeter()
if choose_shape == 2:
    rectangle_cal = rectangle()
    operation = int(input("Press 1 for calculate area,Press 2 for calculate perimeter or Press 3 for both:"))
    if operation == 1:
        rectangle_cal.calculate_area()
    elif operation == 2:
        rectangle_cal.calculate_perimeter()
    elif operation == 3:
        rectangle_cal.calculate_area()
        rectangle_cal.calculate_perimeter()

if choose_shape == 3:
    triangle_cal = triangle()
    operation = int(input("Press 1 for calculate area,Press 2 for calculate perimeter or Press 3 for both:"))
    if operation == 1:
        triangle_cal.calculate_area()
    elif operation == 2:
        triangle_cal.calculate_perimeter()
    elif operation == 3:
        triangle_cal.calculate_area()
        triangle_cal.calculate_perimeter()
