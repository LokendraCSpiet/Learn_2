"""
Exercise 5: Error Handling
Task:
1.	Write a Python function that takes two numbers and divides the first by the second.
2.	Use a try-except block to handle any potential division by zero errors and
print an appropriate message.
"""


def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


# Example usage:
num1 = 10
num2 = 0

# Attempt to divide num1 by num2
result = divide_numbers(num1, num2)

# Check if result is valid (not None) before printing
if result is not None:
    print(f"Result of {num1} divided by {num2} is: {result}")
