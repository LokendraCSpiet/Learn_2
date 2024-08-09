"""
The Knight's Tour Problem (Problem Type: Path Finding)
Problem: The Knight's tour problem is a classic example of the backtracking algorithm
Given an N x N chessboard and a knight placed on the board,
the task is to find a sequence of moves for the knight such that
it visits every square on the board exactly once

"""


def is_safe(x, y, board, N):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


def solve_knight_tour(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    board[0][0] = 0

    def solve(x, y, move_i):
        if move_i == N * N:
            return True

        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if is_safe(nx, ny, board, N):
                board[nx][ny] = move_i
                if solve(nx, ny, move_i + 1):
                    return True
                board[nx][ny] = -1
        return False

    if solve(0, 0, 1):
        for row in board:
            print(row)
        return True
    else:
        print("No solution found")
        return False


# Usage
solve_knight_tour(8)
