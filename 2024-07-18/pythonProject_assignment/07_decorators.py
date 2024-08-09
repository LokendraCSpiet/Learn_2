"""
Exercise 7: Decorators
Task:
1.	Write a decorator function that prints "Function executed" before and after the
    execution of any function it decorates.
2.	Use this decorator to decorate a function that takes two numbers and returns their sum.
"""


def print_executed(func):
    def wrapper(*args, **kwargs):
        print("Function executed")
        result = func(*args, **kwargs)
        print("Function finished execution")
        return result
    return wrapper


@print_executed
def sum_numbers(a, b):
    return a + b


# Example usage:
result = sum_numbers(3, 5)
print("Sum:", result)

