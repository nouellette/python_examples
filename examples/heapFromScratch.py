class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    # Insert a new element into the heap
    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    # Heapify-up (bubble-up)
    def _bubble_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # Extract the minimum element from the heap
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Replace root with the last element
        self._bubble_down(0)  # Heapify-down
        return root

    # Heapify-down (bubble-down)
    def _bubble_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._bubble_down(smallest)

# Example usage:
heap = MinHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
heap.insert(40)

print("Min-Heap:", heap.heap)  # Output: [5, 30, 10, 40, 20]

print("Extracted min:", heap.extract_min())  # Output: 5
print("Min-Heap after extraction:", heap.heap)  # Output: [10, 30, 20, 40]