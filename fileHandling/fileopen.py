import os

# # Specify the file path
file_path = 'file.txt'

# # Check if the file exists before deleting it
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print(f"The file '{file_path}' has been deleted.")
else:
    print(f"The file '{file_path}' does not exist.")
 







# open a file in read mode
# file1 = open("file01.txt",'r')


# read the file content
# read_content = file1.read()
# print(read_content)


# Open the file2.txt in write mode
# file2 = open('file01.txt', 'w')

# Write contents to the file2.txt file
# file2.write('Programming is Fun.\n')
# file2.write('Programiz for beginners\n')

# Close the file after writing
# file2.close()

# Reopen the file2.txt in read mode
# file2 = open('file02.txt', 'r')

# Read the content of file2.txt
# read_content = file2.read()

# # Print the content
# print(read_content)

# Close the file after reading
# file2.close()
