number=int(input("Enter the numbers:"))
temp=number
reverse=0
while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
# print("Reversed number:",reverse )    
    
if temp==reverse:
    print("palindrome")    
else:
    print("not palindrome")    