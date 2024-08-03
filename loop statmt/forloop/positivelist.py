# Input the limit of the list
n = int(input("Enter the limit of the list: "))

# Create and populate the list
numbers = []
for i in range(n):
    x = int(input("Enter an element: "))
    numbers.append(x)

# Print the entered list
print("Entered list:", numbers)

# Print positive numbers in the list
print("Positive numbers in the list:")
for num in numbers:
    if num > 0:
        print(num)
