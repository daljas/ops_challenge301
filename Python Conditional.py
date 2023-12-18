"""
Author: Jason Dallas
Date of latest revision: 12/17/2023
Purpose: Python Conditional
"""

import time

def con_test(a, b):
    # Basic conditionals
    for condition in ["equal to", "not equal to", "less than", "less than or equal to", "greater than", "greater than or equal to"]:
        if eval(f"a {condition.replace(' ', '')} b"):
            print(f"a is {condition} b")

    # Type checking
    for data_type in [bool, str, int]:
        if isinstance(b, data_type):
            print(f"b is a {data_type.__name__}.")

    # Combined conditions
    for val, var in [(a, 'a'), (b, 'b')]:
        if 0 < val < 10:
            print(f"{var} is a positive integer between 0 and 10")

def tests():
    for idx, (a, b) in enumerate([(1, 2), (3, 3), (5, 4)], start=1):
        print(f"\nTEST {idx}\n{'-' * 32}\na = {a}\tb = {b}\n{'-' * 32}")
        con_test(a, b)
        print("-" * 32)
        time.sleep(1.5)

def input_test():
    print("\nUSER INPUT TEST\n{'-' * 32}")
    x, y = int(input("Enter a number for variable a: ")), int(input("Enter a number for variable b: "))
    print("-" * 32)
    con_test(x, y)
    print("-" * 32)

if __name__ == "__main__":
    tests()
    input_test()
