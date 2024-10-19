# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Value of the node
        self.left = None  # Left child
        self.right = None  # Right child

# Define the BinaryTree class (optional)
class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)  # The tree starts with a root node

    # Method to insert nodes (binary search tree style)
    def insert(self, data):
        self._insert_recursive(self.root, data)

    # Helper method to insert recursively
    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    # Method to traverse the tree in-order (Left -> Root -> Right)
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)  # Traverse the left subtree
            print(node.data, end=" ")  # Visit the root
            self.inorder_traversal(node.right)  # Traverse the right subtree

# Example usage
tree = BinaryTree(10)  # Create a tree with root node value 10
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

print("In-order Traversal:")
tree.inorder_traversal(tree.root)  # Output: 3 5 7 10 12 15 18