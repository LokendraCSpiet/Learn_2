def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [5, 2, 9, 1, 5, 6]

index = linear_search(arr, 9)
print(index)  # Output: 2

index = linear_search(arr, 7)
print(index)  # Output: -1
