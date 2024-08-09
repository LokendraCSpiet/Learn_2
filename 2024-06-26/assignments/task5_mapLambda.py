"""
Task 5: Use map() with a lambda function to convert all strings in a list to uppercase.
"""

my_list = ['hello', 'how', 'are', 'you']
mapped = map(lambda x: x.upper(), my_list)
print(list(mapped))
