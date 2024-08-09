"""
Exercise 9: List and Dictionary Combinations
Task:
1.	Create a dictionary where the keys are strings and the values are lists of integers.
2.	Write a function that takes this dictionary and returns a new dictionary where each list
of integers is replaced by its sum.
"""

# Task 1: Create a dictionary with strings as keys and lists of integers as values
example_dict = {
    "numbers1": [1, 2, 3, 4, 5],
    "numbers2": [10, 20, 30],
    "numbers3": [7, 8, 9, 10]
}


# Task 2: Function to replace each list of integers with its sum
def replace_lists_with_sum(d):
    return {key: sum(value) for key, value in d.items()}


sum_dict = replace_lists_with_sum(example_dict)
print(sum_dict)
