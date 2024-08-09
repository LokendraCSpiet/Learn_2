"""
Exercise 6: Regular Expressions
Task:
1.	Write a Python function that takes a string and uses a regular expression to check
if the string is a valid email address.
2.	Write a Python function that takes a string and uses a regular expression to find all
the words that start with a vowel.
"""

import re


def is_valid_email(email):
    # Regular expression for validating an email address
    pattern = r'^[\w\.-]+@[a-zA-Z\d]+\.[a-zA-Z]{2,}$'

    # Using re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


# Example usage:
email1 = "example@email.com"
email2 = "invalid-email"

print(f"Is '{email1}' a valid email address? {is_valid_email(email1)}")
print(f"Is '{email2}' a valid email address? {is_valid_email(email2)}")


def find_vowel_words(text):
    # Regular expression to find words starting with a vowel
    pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'

    # Using re.findall to find all matches in the text
    vowel_words = re.findall(pattern, text)
    return vowel_words


# Example usage:
text = "Apples are delicious. Orange you glad? Elephant in the room."

vowel_words = find_vowel_words(text)
print("Words starting with a vowel:", vowel_words)
