class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = {node: False for node in self.graph}
        rec_stack = {node: False for node in self.graph}

        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

    def add_edge_and_check(self, u, v):
        # Add the edge temporarily
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

        # Check if the graph contains a cycle
        if self.is_cyclic():
            # If a cycle is found, remove the edge
            self.graph[u].remove(v)
            print(f"Edge {u} -> {v} creates a cycle. It was not added.")
            return False
        else:
            print(f"Edge {u} -> {v} was added successfully.")
            return True

    def __str__(self):
        return str(self.graph)


# Usage example
graph = Graph()
graph.add_edge_and_check(1, 2)
graph.add_edge_and_check(2, 3)
graph.add_edge_and_check(3, 4)
graph.add_edge_and_check(4, 2)  # This will create a cycle
print(graph)
