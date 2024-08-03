n = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1  


while b < n:

    print(b)

    a, b = b, a+b 