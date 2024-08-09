"""
Task 4: Graph Edge Addition Validation
Given a directed graph in Python, write a function that adds an edge between two nodes and then
checks if the graph still has no cycles. If a cycle is created, the edge should not be added.
"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, stack):
        visited[v] = True
        stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, stack):
                    return True
            elif stack[neighbor]:
                return True

        stack[v] = False
        return False

    def is_cyclic(self):
        visited = {node: False for node in self.graph}
        stack = {node: False for node in self.graph}

        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, stack):
                    return True

        return False

    def add_edge_check_cycle(self, u, v):
        # Add the edge first
        self.add_edge(u, v)

        # Check if adding the edge creates a cycle
        if self.is_cyclic():
            # If it creates a cycle, remove the edge
            self.graph[u].remove(v)
            print(f"Edge ({u} -> {v}) creates a cycle. Not added.")
        else:
            print(f"Edge ({u} -> {v}) added successfully.")


# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

g.add_edge_check_cycle(0, 3)  # This should add successfully
g.add_edge_check_cycle(3, 0)  # This should not be added due to cycle

# Check the final graph structure
print("Graph after operations:")
print(g.graph)
