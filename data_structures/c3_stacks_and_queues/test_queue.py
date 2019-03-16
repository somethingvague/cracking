import unittest
from data_structures.c3_stacks_and_queues.queue import Queue


class TestQueue(unittest.TestCase):
    def test_remove_raises_IndexError_when_queue_is_empty(self):
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.remove()

    def test_peek_raises_IndexError_when_queue_is_empty(self):
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_add_remove_and_peek(self):
        queue = Queue()
        first_data = 2
        second_data = 4
        queue.add(first_data)
        queue.add(second_data)

        self.assertEqual(queue.remove(), first_data)
        self.assertEqual(queue.peek(), second_data)
        self.assertEqual(queue.remove(), second_data)


if __name__ == "main":
    unittest.main()
