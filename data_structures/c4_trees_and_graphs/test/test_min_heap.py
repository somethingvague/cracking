import unittest

from data_structures.c4_trees_and_graphs.structures.min_heap import MinHeap


class TestMinHeap(unittest.TestCase):
    def test_insert_appends_data(self):
        data = 3
        heap = MinHeap()
        heap.insert(data)
        self.assertEqual(heap._store[1], data)

    def test_insert_preserves_heap_order(self):
        heap = MinHeap()
        heap.insert(4)  # 4
        heap.insert(5)  # 4 5
        heap.insert(3)  # 3 5 4
        heap.insert(2)  # 2 3 4 5

        self.assertEqual(heap._store[1], 2)
        self.assertEqual(heap._store[2], 3)
        self.assertEqual(heap._store[3], 4)
        self.assertEqual(heap._store[4], 5)

    def test_find_min_raises_IndexError_when_heap_is_empty(self):
        with self.assertRaises(IndexError):
            MinHeap().find_min()

    def test_find_min_returns_the_minimum_data(self):
        minimum = 0
        heap = MinHeap()
        heap.insert(42)
        heap.insert(minimum)
        heap.insert(1)

        self.assertEqual(heap.find_min(), minimum)

    def test_extract_min_raises_IndexError_when_heap_is_empty(self):
        with self.assertRaises(IndexError):
            MinHeap().extract_min()

    def test_extract_min_maintains_the_heap_order(self):
        heap = MinHeap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        heap.insert(4)
        heap.insert(5)

        self.assertEqual(heap.extract_min(), 1)
        self.assertEqual(heap.find_min(), 2)

        self.assertEqual(heap.extract_min(), 2)
        self.assertEqual(heap.find_min(), 3)

    def test_size_increments_on_insertion(self):
        heap = MinHeap()
        self.assertEqual(heap.size, 0)

        heap.insert(12)
        self.assertEqual(heap.size, 1)

        heap.insert(42)
        self.assertEqual(heap.size, 2)

    def test_size_decrements_on_extract_min(self):
        heap = MinHeap()
        heap.insert(1)
        heap.insert(2)

        self.assertEqual(heap.size, 2)

        heap.extract_min()
        self.assertEqual(heap.size, 1)

        heap.extract_min()
        self.assertEqual(heap.size, 0)


if __name__ == 'main':
    unittest.main()
