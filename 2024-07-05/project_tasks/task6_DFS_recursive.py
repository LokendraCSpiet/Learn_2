"""
Task 6: Depth-First Search (DFS) Recursive
Write a recursive DFS function in Python for a given undirected graph.
The function should visit every node and print it out.
"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # for undirected graph

    def dfs_recursive(self, start_node, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_node)
        print(start_node, end=" ")

        for neighbor in self.graph[start_node]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)


# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS recursive starting from node 0:")
g.dfs_recursive(0)
