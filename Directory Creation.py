#!/usr/bin/env python3

# Import libraries
import os

# Declaration of functions
def generate_directory_structure(user_path):
    for (root, dirs, files) in os.walk(user_path):
        print("==root==")
        print(root)
        print("==dirs==")
        print(dirs)
        print("==files==")
        print(files)

# Main
if __name__ == "__main__":
    # Read user input into a variable
    user_input_path = input("Enter the directory path: ")

    # Call the function with user input
    generate_directory_structure(user_input_path)
