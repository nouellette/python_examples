class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store graph

    def add_edge(self, u, v):
        # Add an edge from vertex u to v.
        # If u is not in the graph, add u with an empty list.
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        # Utility function used by DFS
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph.get(v, []):
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):
        # Perform DFS starting from vertex v
        visited = set()  # Set to store visited vertices
        self.dfs_util(v, visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS starting from vertex 2:")
g.dfs(2)