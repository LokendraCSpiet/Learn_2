"""
Bubble Sort (Brute Force Approach):
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements, and swaps them if they are in the wrong order.
The pass through the list is repeated until the list is sorted.
The algorithm gets its name because smaller elements "bubble" to the top of the list.

Complexity:
    Time Complexity  : O(n^2) in the worst and average cases, O(n) in the best case (when the list is already sorted).
    Space Complexity : O(1) (in-place sorting).
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array using Bubble Sort:", sorted_arr)