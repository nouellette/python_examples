class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        dequeued_value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return dequeued_value

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


queue = LinkedListQueue()
queue.enqueue(1)
queue.enqueue(1)
queue.dequeue()
print(queue.size())