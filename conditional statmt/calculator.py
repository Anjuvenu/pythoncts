num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
ope=input("Enter a operator:")


if ope=='+':
    result=num1+num2
elif ope=='-':
    result=num1-num2
elif ope=='*':
    result=num1*num2
elif ope=='/':
    result=num1/num2

else:
    result="invalid ope"                

print(result)    