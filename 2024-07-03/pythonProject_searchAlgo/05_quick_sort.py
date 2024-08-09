"""
1. Initial Array
[64, 34, 25, 12, 22, 11, 90]

2. First Call to Quick Sort:
- Pivot: 25 (middle element)
- Partition into three sub-arrays:
    Left: [12, 22, 11] (elements less than pivot)
    Middle: [25] (elements equal to pivot)
    Right: [64, 34, 90] (elements greater than pivot)
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # Output [11, 12, 22, 25, 34, 64, 90]
