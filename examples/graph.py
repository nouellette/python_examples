class Node:
    def __init__(self, data):
        self.data = data
        self.adjacent = []  # List to store adjacent nodes

    def add_adjacent(self, node):
        self.adjacent.append(node)
        # For an undirected graph, you might want to add this node to the adjacent list of 'node' as well

class Graph:
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes

    def add_node(self, key, data):
        if key not in self.nodes:
            self.nodes[key] = Node(data)

    def add_edge(self, key1, key2):
        if key1 in self.nodes and key2 in self.nodes:
            self.nodes[key1].add_adjacent(self.nodes[key2])
            # For an undirected graph, also add the reverse edge
            # self.nodes[key2].add_adjacent(self.nodes[key1])

    def display(self):
        for key, node in self.nodes.items():
            print(f"Node {key}: {node.data}, Adjacent: {[n.data for n in node.adjacent]}")

# Example usage
g = Graph()
g.add_node(1, "A")
g.add_node(2, "B")
g.add_node(3, "C")
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.display()