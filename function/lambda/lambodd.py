
n = int(input("Enter the limit of the list: "))


li = []
for i in range(n):
    x = int(input("Enter an element: "))
    li.append(x)


print("Entered list:", li)

 
final_list = list(filter(lambda y: (y % 2 != 0), li))
print("Odd numbers are:",final_list)