
even = 0
odd = 0
num = 1  


print("First 10 even numbers:")
while even < 10:
    if num % 2 == 0:
        print(num, end=", ")
        even += 1
    num += 1


num = 1
even = 0


print("\nFirst 10 odd numbers:")
while odd < 10:
    if num % 2 != 0:
        print(num, end=", ")
        odd += 1
    num += 1