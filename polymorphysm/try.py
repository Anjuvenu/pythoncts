def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

try:
    numbers = []
    while True:
        num = input("Enter a number (or 'done' to finish): ")
        if num.lower() == 'done':
            break
        numbers.append(float(num))

    if not numbers:
        raise ValueError("You must enter at least one number.")

    average = calculate_average(numbers)
    print("Average:", average)

except ValueError as ve:
    print("Error:", ve)
except ZeroDivisionError:
    print("Error: Cannot calculate average of an empty list.")
except Exception as e:
    print("An unexpected error occurred:", e)