# main.py


from math_operations import arithmetic, trigonometry


num1 = float(input("Enter a value for number1: "))
num2= float(input("Enter a value for number2: "))

# Arithmetic operations
print("Addition:", arithmetic.add(num1,num2))      
print("Subtraction:", arithmetic.subtract(num1,num2))  
print("Multiplication:", arithmetic.multiply(num1,num2)) 
print("Division:", arithmetic.divide(num1,num2))    

# Take input from the user
x = float(input("Enter a value for x: "))
y = float(input("Enter a value for y: "))

# Trigonometric operations
print("Sine:", trigonometry.sine(x)) 
print("Cosine:", trigonometry.cosine(y)) 
print("Tangent:", trigonometry.tangent(x/y))


