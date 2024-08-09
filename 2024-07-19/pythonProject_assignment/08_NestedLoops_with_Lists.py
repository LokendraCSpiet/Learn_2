"""
Exercise 8: Nested Loops with Lists
Task:
1.	Create a 5x5 matrix (list of lists) initialized with zeros.
2.	Write a Python function that takes this matrix and fills it with a pattern like a checkerboard
(alternating 1s and 0s).
"""


# Task 1: Create a 5x5 matrix initialized with zeros
def create_zero_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


# Task 2: Fill the matrix with a checkerboard pattern
def fill_checkerboard(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            # Check if the sum of row index and column index is even or odd
            if (i + j) % 2 == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0


# Example usage:
matrix = create_zero_matrix(5, 5)
fill_checkerboard(matrix)

for row in matrix:
    print(row)


