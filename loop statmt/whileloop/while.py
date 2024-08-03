# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

# 1.Print i as long as i is less than 6:

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# 2.Sum of numbers up to limit:

# i=int(input("enter the limit:"))
# sum = 0
# num = 1
# while num <= i:
#     sum += num
#     num += 1
# print("Sum:", sum)


# 3.Print even numbers up to n numbers:

# i=int(input("enter the limit:"))
# num = 2
# while num <=i:
#     print(num)
#     num += 2

# 4.Multiplication table:

num = int(input("Enter the number:"))
i = 1

while i <= 10:
    result = num * i
    print(f"{num} x {i} = {result}")#It then prints the multiplication equation using an f-string
    i += 1

# 5.Fibonacci sequence up to limit:

# i=int(input("Enter the limit:"))
# a, b = 0, 1
# while a <= i:
#     print(a, end=" ")
#     a, b = b, a + b