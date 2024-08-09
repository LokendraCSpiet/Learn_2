"""
Rat in a Maze (Problem Type: Path Finding)
Problem: Given a maze represented as an N x N matrix,
find a path from the top-left corner to the bottom-right corner.
The path can only be made through cells that are not blocked (represented by 1).

"""


def is_safe(maze, x, y, sol, N):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 1 and sol[x][y] == 0


def solve_rat_maze(maze):
    N = len(maze)
    sol = [[0 for _ in range(N)] for _ in range(N)]

    def solve(x, y):
        if x == N - 1 and y == N - 1:
            sol[x][y] = 1
            return True

        if is_safe(maze, x, y, sol, N):
            sol[x][y] = 1
            if solve(x + 1, y):
                return True
            if solve(x, y + 1):
                return True
            sol[x][y] = 0
        return False

    if solve(0, 0):
        for row in sol:
            print(row)
        return True
    else:
        print("No solution found")
        return False


# Usage
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
solve_rat_maze(maze)
