num = int(input("Enter the number:"))

def armstrong(num):


        sum = 0

        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10

        if num == sum:
             print(num,"is an Armstrong number")
        else:
         print(num,"is not an Armstrong number") 

armstrong(num)
         