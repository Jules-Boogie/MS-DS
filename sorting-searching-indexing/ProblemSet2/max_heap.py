class MaxHeap:
    def __init__(self):
        self.H = [None]
        
    def size(self):
        return len(self.H)-1
    
    def __repr__(self):
        return str(self.H[1:])
        
    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] <= self.H[i//2],  f'Maxheap property fails at position {i//2}, parent elt: {self.H[i//2]}, child elt: {self.H[i]}'
    
    def max_element(self):
        return self.H[1]
    
    def bubble_up(self, index):
        assert index >= 1
        if index == 1:
            return
        parent = index//2 
        if self.H[parent] > self.H[index]:
            return
        if self.H[parent] < self.H[index]:
            self.H[parent], self.H[index] = self.H[index], self.H[parent]
            self.bubble_up(parent)

        
            
    
    def bubble_down(self, index):
        assert index >=1 and index < len(self.H)
        left = 2 * index
        right = 2 * index + 1
        print(left,right)
        left_child = self.H[left] if left < len(self.H) else float('-inf')
        right_child = self.H[right] if right < len(self.H) else float('-inf')
        if self.H[index] >= max(left_child,right_child):
            return
        max_child, max_index = max((left_child,left),(right_child, right))
        self.H[index],self.H[max_index] = self.H[max_index], self.H[index]
        self.bubble_down(max_index)
        
        
        
    
    # Function: insert
    # Insert elt into minheap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        self.H.append(elt)
        self.bubble_up(len(self.H)-1)
        
        
    # Function: delete_max
    # delete the largest element in the heap. Use bubble_up/bubble_down
    def delete_max(self):
        if self.size() == 1:
            self.H = []
        else:
            self.H = self.H[1:]
            self.bubble_down(1)

h = MaxHeap()
print('Inserting: 5, 2, 4, -1 and 7 in that order.')
h.insert(5)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(2)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(4)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(-1)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(7)
print(f'\t Heap = {h}')
assert(h.max_element() == 7)
h.satisfies_assertions()

print('Deleting maximum element')
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 4)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 2)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == -1)
# Test delete_max on heap of size 1, should result in empty heap.
h.delete_max()
print(f'\t Heap = {h}')
print('All tests passed: 5 points!')        