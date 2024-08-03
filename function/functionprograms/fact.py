# def fact(x):
#     if x==1:
#         return 1
#     else:
#         return(x*fact(x-1))
    
# num=5
# print("factorial if",num,"is",fact(num))    

number=int(input("Enter the number:"))
def fact(x):
    f=1
    for i in range(1,x+1):
        f*=i
    return f
obj=fact(number)  
print(obj)  
