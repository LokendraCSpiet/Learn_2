"""
Exercise 8: Data Structures
Task:
1.	Implement a stack using a list with methods for push, pop, and peek.
2.	Implement a queue using a list with methods for enqueue, dequeue, and peek.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack peek:", stack.peek())  # Output: 3

print("Pop item from stack:", stack.pop())  # Output: 3
print("Stack peek after pop:", stack.peek())  # Output: 2


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


# Example usage:
queue = Queue()

queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print("Queue peek:", queue.peek())  # Output: 'a'

print("Dequeue item from queue:", queue.dequeue())  # Output: 'a'
print("Queue peek after dequeue:", queue.peek())  # Output: 'b'
