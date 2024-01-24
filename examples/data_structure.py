import heapq

class MedianHeap:
    def __init__(self):
        self.max_heap = []  # max heap for lower half
        self.min_heap = []  # min heap for upper half

    def add(self, num):
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)  # max heap is implemented as a min heap with negated values
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

# Example usage
median_heap = MedianHeap()
median_heap.add(3)
median_heap.add(1)
median_heap.add(4)
median_heap.add(2)

print("Median:", median_heap.find_median())  # Should be 2.5 in this case (average of 2 and 3)
