x=int(input("Enter the number:"))
factorial=lambda n:1 if n==0 else n*factorial(n-1)
print(factorial(x))