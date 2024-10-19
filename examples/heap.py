import heapq

# Create an empty heap
heap = []

# Insert elements into the heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
heapq.heappush(heap, 30)
heapq.heappush(heap, 40)

print("Heap after insertions:", heap)  # Output: [5, 20, 10, 30, 40]

# Extract the smallest element (min-heap root)
smallest = heapq.heappop(heap)
print("Extracted smallest element:", smallest)  # Output: 5
print("Heap after extraction:", heap)  # Output: [10, 20, 40, 30]

# Peek at the smallest element without removing
smallest_peek = heap[0]
print("Smallest element (peek):", smallest_peek)  # Output: 10