def travelling_salesman_problem(graph, start):
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1 << start][start] = 0

    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                for j in range(n):
                    if mask & (1 << j) == 0:
                        dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + graph[i][j])

    return min(dp[(1 << n) - 1][i] + graph[i][start] for i in range(n))


# Usage
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start = 0  # Starting point A
print(travelling_salesman_problem(graph, start))
