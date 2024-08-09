import math


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


# Usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(jump_search(arr, 15))  # Output: 7
print(jump_search(arr, 20))  # Output: -1
