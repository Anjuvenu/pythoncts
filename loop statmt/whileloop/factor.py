number=int(input("Enter the number:"))
factor=1
print("factors of",number,"are:")
while factor<=number:
    if number%factor==0:  
        print(factor)
    factor+=1
