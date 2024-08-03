def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


print("Select Operation")

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")



num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

choice=input("Enter the choice(1/2/3/4):")


if choice=="1":
    print("Result:",add(num1,num2))

elif choice=="2":
    print("Result:",sub(num1,num2))

elif choice=="3":
    print("Result:",mul(num1,num2))   

elif choice=="4":
    print("Result:",div(num1,num2))  

else:
    print("Invalid Input")


