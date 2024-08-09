"""
Exercise 5: Functions and Error Handling
Task:
1.	Write a function that takes two arguments, a and b, and returns their division.
Handle the case where division by zero might occur and print an appropriate message.
2.	Modify the function to raise a custom exception if either of the arguments is not a number.
"""


# Task 1: Function for division with zero division handling
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    return result


num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
result = divide(num1, num2)
if result is not None:
    print(f"The result of {num1} divided by {num2} is {result}")


# Task 2: Function with custom exception for non-numeric arguments
class NonNumericError(Exception):
    pass


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise NonNumericError("Both arguments must be numbers.")

    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    return result


# Example usage:
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = divide(num1, num2)
    if result is not None:
        print(f"The result of {num1} divided by {num2} is {result}")
except NonNumericError as e:
    print(e)
except ValueError:
    print("Error: Please enter valid numbers.")
