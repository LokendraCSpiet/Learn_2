"""
N Queen Problem (Problem Type: Arrangement)
Problem: Place N queens on an N x N chessboard such that
no two queens threaten each other
"""


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    def solve(col):
        if col >= N:
            return True
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                if solve(col + 1):
                    return True
                board[i][col] = 0
        return False

    if solve(0):
        for row in board:
            print(row)
        return True
    else:
        print("No solution found")
        return False


# Usage
solve_n_queens(8)
