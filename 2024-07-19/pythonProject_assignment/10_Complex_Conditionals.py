"""
Exercise 10: Complex Conditionals
Task:
1.	Write a Python program that takes a list of integers and separates the list into two lists:
one containing even numbers and the other containing odd numbers.
2.	Write a function that takes these two lists and merges them, alternating between elements from
each list.
"""


# Task 1: Separate a list into even and odd numbers
def separate_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers


numbers = [10, 15, 23, 42, 57, 68, 91]
even_numbers, odd_numbers = separate_even_odd(numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


# Task 2: Merge two lists, alternating between elements
def merge_alternating(even_list, odd_list):
    merged_list = []
    max_length = max(len(even_list), len(odd_list))

    for i in range(max_length):
        if i < len(even_list):
            merged_list.append(even_list[i])
        if i < len(odd_list):
            merged_list.append(odd_list[i])

    return merged_list


merged_list = merge_alternating(even_numbers, odd_numbers)
print("Merged list:", merged_list)
