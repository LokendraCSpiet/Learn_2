"""
Task 2: Implementing Queues in Python
Definition and types: Simple, Circular, Priority, Double Ended
Basic operations: Enqueue, Dequeue, Peek, isEmpty
"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


# Usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())  # Output: 1
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.is_empty())  # Output: False
print(queue.dequeue())  # Output: 3
print(queue.is_empty())  # Output: True
