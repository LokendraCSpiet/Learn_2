"""
Exercise 1: Nested Loops and Conditionals
Task:
1.	Write a Python program that prints a multiplication table for numbers 1 to 10.
2.	Modify the program to print only the products that are even numbers.
"""

# Task 1: Multiplication table for numbers 1 to 10
for i in range(1, 11):  # i will range from 1 to 10
    for j in range(1, 11):  # j will range from 1 to 10
        product = i * j
        print(f"{i} * {j} = {product}")


# Task 2: Multiplication table with only even products
for i in range(1, 11):  # i will range from 1 to 10
    for j in range(1, 11):  # j will range from 1 to 10
        product = i * j
        if product % 2 == 0:
            print(f"{i} * {j} = {product}")
