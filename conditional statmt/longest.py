num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


if num1 >= num2 and num1 >= num3:
    longest_number = num1
elif num2 >= num1 and num2 >= num3:
    longest_number = num2
else:
    longest_number = num3


print("The longest number is:", longest_number)