"""
Exercise 2: Advanced List Comprehensions
Task:
1.	Create a list of all the numbers from 1 to 100 that are divisible by both 3 and 5
using a list comprehension.
2.	Create a list of tuples, where each tuple contains a number from 1 to 10 and its square.
"""

# Task 1: List of numbers from 1 to 100 divisible by both 3 and 5
list1 = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(list1)


# Task 2: List of tuples containing numbers from 1 to 10 and their squares
squares = [(num, num**2) for num in range(1, 11)]
print(squares)
