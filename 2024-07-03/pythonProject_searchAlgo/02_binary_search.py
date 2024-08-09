def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr,6))  # Output: 5
print(binary_search(arr, 10))  # Output: -1


"""
1. Search for 6:
    Initial array: "[1, 2, 3, 4, 5, 6, 7, 8, 9]
    Initial 'left': 0, 'right': 8
    Calculate "mid": "4" (index of value 5)
    Since arr[mid] (5) is less than target (6), set left to 'mid+1 (5)
    New "left": 5, "right":8
    Calculate new "mid":6 (index of value 7)
    Since arr[mid] (7) is greater than 'target' (6), set right to mid 1 (5)
    New left: 5, right: 5
    Calculate new "mid": "5" (index of value 6)
    Since arr[mid] (6) is equal to target (6), return "mid" (5)
"""