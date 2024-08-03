# define  class called rectangle with attribtes length width and also inculde the methods to calculate area and perimeter
class Rectangle:

    def __init__(self, width, height):
        self.perimeter_of_rectangle = None
        self.area_of_rectangle = None
        self.width_rectangle = width
        self.height_rectangle = height

    def area(self):
        self.area_of_rectangle = self.width_rectangle * self.height_rectangle
        print(f"The area of the rectangle with a height of {self.height_rectangle} and width of {self.width_rectangle} ={self.area_of_rectangle}") 


    def perimeter(self):
        self.perimeter_of_rectangle = 2 * (self.width_rectangle + self.height_rectangle)
        print(f"The perimeter of the rectangle with a height of {self.height_rectangle} and width of {self.width_rectangle} ={self.perimeter_of_rectangle}") 



input_width = int(input("Enter the width of rectangle ="))
input_height = int(input("Enter the height of rectangle ="))
Rectangle_1 = Rectangle(input_width, input_height)
Rectangle_1.area()
Rectangle_1.perimeter()

