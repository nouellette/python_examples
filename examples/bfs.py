from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store graph

    def add_edge(self, u, v):
        # Add an edge from vertex u to v.
        # If u is not in the graph, add u with an empty list.
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start_vertex):
        # Perform BFS starting from vertex start_vertex
        visited = set()  # Set to store visited vertices
        queue = deque([start_vertex])  # Queue for BFS

        # Loop to visit each node
        while queue:
            vertex = queue.popleft()  # Remove the vertex from the queue
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)

                # Add all unvisited neighbors to the queue
                for neighbour in self.graph.get(vertex, []):
                    if neighbour not in visited:
                        queue.append(neighbour)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS starting from vertex 2:")
g.bfs(2)