"""
Task 1: String Operations
Write a Python method that takes two strings, concatenates them, reverses the result,
and then extracts the middle substring of the given length. Ensure your method handles edge cases,
such as an empty string or a substring length larger than the concatenated string.
"""


def string_operations(s1, s2, length):
    # Concatenate the strings
    concatenated = s1 + s2

    # Reverse the concatenated string
    reversed_string = concatenated[::-1]

    # Handle edge cases
    if length <= 0 or length > len(reversed_string):
        return ""

    # Calculate start index to extract the middle substring
    mid = len(reversed_string) // 2
    start_index = max(0, mid - (length // 2))

    # Adjust the start index if the substring exceeds the bounds
    end_index = start_index + length
    if end_index > len(reversed_string):
        start_index = len(reversed_string) - length
        end_index = len(reversed_string)

    # Extract the middle substring of the given length
    middle_substring = reversed_string[start_index:end_index]

    return middle_substring


# Example usage
s1 = "hello"
s2 = "world"
length = 5
result = string_operations(s1, s2, length)
print("Middle substring:", result)


# Edge cases
empty_result = string_operations("", "", 5)
print("Empty string result:", empty_result)

large_length_result = string_operations("hello", "world", 50)
print("Large length result:", large_length_result)

zero_length_result = string_operations("hello", "world", 0)
print("Zero length result:", zero_length_result)
