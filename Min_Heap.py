import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def extract_min(self):
        return heapq.heappop(self.heap) if self.heap else None

# Example Usage
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(1)

print(min_heap.get_min())  # Output: 1
print(min_heap.extract_min())  # Output: 1
print(min_heap.get_min())  # Output: 5
