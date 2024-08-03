n = int(input("Enter the limit of the list: "))
list1 = []

for i in range(n):
    x = int(input("Enter elements: "))
    list1.append(x)

print("Entered list:", list1)

total_sum = 0

for num in list1:
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    total_sum += digit_sum

print("Sum of digits in the list:", total_sum)

