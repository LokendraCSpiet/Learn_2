"""
Merge Sort (Divide and Conquer Approach)
Theory:
Merge Sort is a divide and conquer algorithm that divides the unsorted list into two approximately equal halves, recursively sorts each half, and then merges the two sorted halves to produce the sorted list. It is more efficient than Bubble Sort, especially for larger lists.

Complexity:

Time Complexity: O(n log n) in the worst, average, and best cases.
Space Complexity: O(n) due to the temporary arrays used during the merge process.
"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("Sorted array using Merge Sort:", sorted_arr)