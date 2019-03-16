import unittest

from data_structures.c3_stacks_and_queues.questions.queue_via_stacks import QueueViaStacks


class TestQueueViaStacks(unittest.TestCase):
    def test_remove_raises_IndexError_when_queue_is_empty(self):
        with self.assertRaises(IndexError):
            QueueViaStacks().remove()

    def test_add_remove(self):
        queue = QueueViaStacks()
        first = 1
        second = 2
        third = 3
        queue.add(first)
        queue.add(second)
        self.assertEqual(queue.remove(), first)
        queue.add(third)
        self.assertEqual(queue.remove(), second)
        self.assertEqual(queue.remove(), third)
