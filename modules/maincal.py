import calculator


num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

choice=input("Enter the choice(1.addition/2.Subtraction/3.Multiplication/4.Division):")


if choice=="1":
    print("Result:",calculator.add(num1,num2))

elif choice=="2":
    print("Result:",calculator.sub(num1,num2))

elif choice=="3":
    print("Result:",calculator.mul(num1,num2))   

elif choice=="4":
    print("Result:",calculator.div(num1,num2))  

else:
    print("Invalid Input")