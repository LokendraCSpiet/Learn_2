class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def delete_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_element

    def get_min(self):
        return self.heap[0] if self.heap else None

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] >= self.heap[parent_index]:
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def __str__(self):
        return str(self.heap)


# Usage example
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(6)
min_heap.insert(5)
min_heap.insert(2)
min_heap.insert(4)

print("Heap after insertions:", min_heap)  # Output: [1, 2, 4, 5, 3, 6]
print("Minimum element:", min_heap.get_min())  # Output: 1
print("Deleted minimum element:", min_heap.delete_min())  # Output: 1
print("Heap after deletion:", min_heap)  # Output: [2, 3, 4, 5, 6]
