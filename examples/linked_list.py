class Node:
    def __init__(self, data):
        self.data = data  # The data part
        self.next = None  # The pointer part, initially None

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:
            self.head = new_node  # If the list is empty, make the new node the head
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Append the new node at the end

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)

llist.display()