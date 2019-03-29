"""Custom binary heap implementation where the minimum element is the root.

Allows enqueueing and dequeueing in O(log n)

Ensures the following properties:
 * Structure: the tree is balanced, so we create a 'complete binary tree' where there every level of the
   tree is filled, except maybe the last level. The levels are populated from left to right.
 * Heap order: for every node 'x' with parent 'p', p <= x
"""


class MinHeap:
    """Min Heap implementation backed by a single array"""
    def __init__(self):
        # the root node will occupy 2 indices so that we can compute the parent of any node with integer division
        self._store = [0]
        self.size = 0

    def extract_min(self):
        """Removes and returns the minimum value in the heap in 0(1) time whilst maintaining the heap order property"""
        minimum = self.find_min()
        self._store[1] = self._store[self.size]  # Replace root with final element
        self.size -= 1
        self._percolate_down()  # Percolate the new root downwards
        return minimum

    def find_min(self):
        """Returns the minimum data in the heap

        Raises:
            IndexError if the heap is empty
        """
        if self.size == 0:
            raise IndexError('The heap is empty')

        return self._store[1]

    def insert(self, data):
        """Inserts new item onto the heap and moves it in a position which maintains
        the heap order property

        Args:
            data: data to be inserted into the heap
        """
        self._store.append(data)
        self.size += 1
        self._percolate_up()

    def _percolate_up(self):
        """Moves the inserted data up the heap to maintain the heap order"""
        index = self.size
        while index // 2 > 0:  # stop if we get to the root
            parent = self._store[index // 2]
            if self._store[index] < parent:
                self._store[index // 2] = self._store[index]
                self._store[index] = parent
                index = index // 2
            else:
                index = 0  # Stop iterating

    def _percolate_down(self):
        """Moves the root index down the heap to maintain the heap order"""
        index = 1  # root element
        while index * 2 <= self.size:
            minimum_child_index = self._find_minimum_child_index(index)
            if self._store[index] > self._store[minimum_child_index]:
                # Swap the data with the minimum child
                tmp = self._store[minimum_child_index]
                self._store[minimum_child_index] = self._store[index]
                self._store[index] = tmp
                index = minimum_child_index
            else:
                index = self.size  # Stop iterating

    def _find_minimum_child_index(self, index):
        """Returns the index of the minimum child"""
        left_index = index * 2
        right_index = left_index + 1
        if right_index > self.size:
            return left_index  # There is one child only
        else:
            return left_index if self._store[left_index] < self._store[right_index] else right_index
