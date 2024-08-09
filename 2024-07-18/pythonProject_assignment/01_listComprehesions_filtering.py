"""
Exercise 1: List Comprehensions and Filtering
Task:
1.	Create a list of numbers from 1 to 20.
2.	Use a list comprehension to create a new list that contains
only the even numbers from the original list.
3.	Use a list comprehension to create a new list that
contains the squares of the numbers from the original list.
"""

original_list = list(range(1, 21))
print("Original list:", original_list)

even_numbers = [num for num in original_list if num % 2 == 0]
print("Even numbers:", even_numbers)

squares = [num ** 2 for num in original_list]
print("Squares of numbers:", squares)
