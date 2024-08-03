# rows=int(input("Enter the number:"))
# while rows > 0:
#     print('* ' * rows)
#     rows -= 1
 
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print('*', end=" ")
        j += 1
    print()
    i += 1