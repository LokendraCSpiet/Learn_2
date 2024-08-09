"""
Task 1: Implementing Stacks in Python
Definition and characteristics
Basic operations: Push, Pop, Peek, isEmpty
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty (self):
        return len(self.stack) == 0


# Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # Output: 3
print("After Peek: ", stack.stack)
print(stack.pop())  # Output: 3
print("After Pop: ", stack.stack)
