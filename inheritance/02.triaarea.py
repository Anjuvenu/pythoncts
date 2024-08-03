class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Taking input for triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle = Triangle(base, height)
print("Area of Triangle:", triangle.area())  

# Taking input for square
side = float(input("Enter the side of the square: "))
square = Square(side)
print("Area of Square:", square.area())




# class Shape:
#     def area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

# triangle = Triangle(4, 6)
# print("Area of Triangle:", triangle.area())  

# square = Square(5)
# print("Area of Square:", square.area()) 



