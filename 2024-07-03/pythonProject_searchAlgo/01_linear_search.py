def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Usage
arr = [5, 2, 9, 1, 5, 6]
print(linear_search(arr, 9))  # Output: 2
print(linear_search(arr, 7))  # Output: -1


"""
Characteristics:

Time Complexity: O(n)
Best Case: O(1) (when the element is found at the first position)
Worst Case: O(n) (when the element is at the last position or not present)
Data Structure: Works on both sorted and unsorted data
"""