num=int(input("Enter the number:"))
def palindrome(num):
    rev=0
    temp=num
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if temp==rev:
        print("palindrome")    
    else:
       print("not palindrome")    

palindrome(num)        