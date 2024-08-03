class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Taking input for rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
rectangle = Rectangle(length, breadth)
print("Area of Rectangle:", rectangle.area())  

# Taking input for circle
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print("Area of Circle:", circle.area())



# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# rectangle = Rectangle(5, 4)
# print("Area of Rectangle:", rectangle.area())  

# circle = Circle(3)
# print("Area of Circle:", circle.area()) 


