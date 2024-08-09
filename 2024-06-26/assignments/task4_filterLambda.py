"""
Task 4: Create a filter using a lambda function that extracts all words from a list that
have more than 4 characters.
"""

my_list = ['Lucky', 'Arya', 'is', 'a', 'Good', 'Student']
filtered = filter(lambda x: len(x) > 4, my_list)
print(list(filtered))
