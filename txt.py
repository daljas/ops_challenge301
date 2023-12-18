# Create a new .txt file and append three lines
with open('example.txt', 'w') as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Read and print the first line from the created file
with open('example.txt', 'r') as file:
    first_line = file.readline()
    print("First Line:", first_line)

# Delete the .txt file
import os
os.remove('example.txt')
