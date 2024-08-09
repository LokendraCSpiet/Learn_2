import heapq


def heap_sort(arr):
    heapq.heapify(arr)  # Transform List into a heap, in-place, in linear time
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr


# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = heap_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 34, 64, 90]

