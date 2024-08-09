import array

# Creating an array of integer
arr = array.array('i',[1, 2, 3, 4, 5])
print(arr)

arr = [1, 2, 3, 4, 5]
print(arr)

print(arr[0])  # Output: 1

print(arr[2])  # Output: 3

arr.insert(2, 99)  # Insert 99 at index 2

print(arr)  # Output: [1, 2, 99, 3, 4, 5]

# Slice
arr[2:2] = [55]  # Insert 99 at index 2

print(arr)  # Output: [1, 2, 99, 3, 4, 5]


# Deleting an element
arr.remove(3)  # Remove the first occurrence of 3
print("After removing 3:", arr)

# Updating an element
arr[1] = 22  # Update the element at index 1 to 22
print("After updating index 1 to 22:", arr)

# Reversing the array
arr.reverse()
print("After reversing the array:", arr)
