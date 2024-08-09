"""
Task 6: Utilize reduce() from functools and a lambda to calculate the factorial
of a number provided in a list.
"""


from functools import reduce

numbers = [3, 2, 5]
facto_list = map(lambda y: reduce(lambda x, z: x*z, range(1, y+1)), numbers)
print(list(facto_list))

