# For Loops
# A for loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set, or a string).
#The for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

#Print each fruit in a fruit list:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# With the break statement we can stop the loop before it has looped through all the items:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":
#     break

#Exit the loop when x is "banana", but this time the break comes before the print:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

#To loop through a set of code a specified number of times, we can use the range() function
# 1.Printing numbers from 1 to 5:

# for i in range(1, 6):
#     print(i)

# 2.Sum of numbers from 1 to 10: 

# num=int(input("Enter the number:"))
# sum = 0
# for i in range(num):
#     sum += i
# print("Sum:", sum)

# 3.Calculate factorial of a number:

#The program calculates it by multiplying 1 * 2 * 3 * 4 * 5.
# n =int(input("Enter the number:"))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print("Factorial:", factorial)

# 4.Count the number of vowels in a word:
# word =input("Enter the word:")
# count = 0
# for char in word:
#     if char.lower() in "aeiou": #checks if the lowercase version of the current character is a vowel (a, e, i, o, u). The lower() method is used to handle both uppercase and lowercase vowels.
        # count += 1 #If the condition is true, it increments the count by 1.
# print("Number of vowels:", count)

# 5.Print multiplication table for a given number:
# num =int(input("Enter the number:"))
# for i in range(1, 11):
#     result = num * i
#     print(f"{num} x {i} = {result}")

#6.Print a pattern:
# n=int(input("Enter the number:"))
# for i in range(n):
#     print('* ' * (i + 1))
# size = 6 

# for i in range(size):
#     for j in range(1,i + 1):
#         print("*", end=" ")
#     print()