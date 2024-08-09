"""
Task 2: Create a custom iterator class Reverselter,
which takes a list and iterates it from the reverse direction.
"""


class Reverselter:
    def __init__(self,data):
        self.listItem = data
        self.size = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.size == 0:
            raise StopIteration
        else:
            self.size -= 1
            return self.listItem[self.size]


my_list = ['a', 'b', 5, 2, 'c']
rev_list = Reverselter(my_list)

for i in rev_list:
    print(i)
