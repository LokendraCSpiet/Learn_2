"""
Task 3: Write a generator function fib gen that yields the Fibonacci sequence up to a given
number n.
"""


def fib_gen(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a+b


n = int(input("Enter number:"))
for num in fib_gen(n):
    print(num)