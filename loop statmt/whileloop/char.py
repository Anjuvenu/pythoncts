input_string = input("Enter a string: ")

# Initialize position variable
position = 0

# Display character positions using a while loop
while position < len(input_string):
    print(f"Character at position {position}: {input_string[position]}")
    position += 1