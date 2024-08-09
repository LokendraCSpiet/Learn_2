def bubble_sort(arr):
    n = len(arr)  # 6
    for i in range(n):  # 5
        for j in range(0, n-i-1):  # iterate through all the elements by excluding 5
            if arr[j] > arr[j+1]:  # 5 > 2
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Compare and Swap
    return arr


arr = [5, 2, 9, 1, 5, 6]

sorted_arr = bubble_sort(arr)

print(sorted_arr)  # Output: [1, 2, 5, 5, 6, 9]
