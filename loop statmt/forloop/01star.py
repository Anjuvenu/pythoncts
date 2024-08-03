rows = 5

# Outer loop for each row
for i in range(rows):
    # Inner loop for printing asterisks in each row
    for j in range(i+1):
        print("*", end=" ")
    # Move to the next line after printing each row
    print()