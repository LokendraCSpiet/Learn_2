'''
Day 8: Comprehension, Iterators, Generator, Decorators, Lambda function

Task 1: Write a list comprehension that creates a list of squares for all even numbers
between 0 and 20.
'''

evens = [num**2 for num in range(0, 21) if num % 2 == 0]
print(evens)
