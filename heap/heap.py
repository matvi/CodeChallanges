from graphviz import Digraph

class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)
    
    def visualize(self):
        dot = Digraph(comment='Binary Heap')
        for i, value in enumerate(self.heap):
            dot.node(str(i), str(value))
            if i > 0:
                parent_index = (i - 1) // 2
                dot.edge(str(parent_index), str(i))
        return dot

# Create a binary heap and insert values
heap = BinaryHeap()
values = [5, 3, 8, 1, 4, 9]
for value in values:
    heap.insert(value)

# Visualize the binary heap
heap_visualization = heap.visualize()
heap_visualization.render("binary_heap", format="png", cleanup=True)
