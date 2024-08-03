number=int(input("Enter the digit:"))
sum=0
while number>0:
    digit=number%10
    sum+=digit
    number//=10
print("the sum of",sum)
