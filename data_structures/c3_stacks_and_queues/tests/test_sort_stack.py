import unittest

from data_structures.c3_stacks_and_queues.questions.sort_stack import sort_stack
from data_structures.c3_stacks_and_queues.stack import Stack


class TestSortStack(unittest.TestCase):
    def test_sort_stack(self):
        stack = Stack()
        stack.push(4)
        stack.push(2)
        stack.push(3)
        stack.push(5)
        stack.push(1)

        sorted_stack = sort_stack(stack)

        self.assertEqual(sorted_stack.pop(), 1)
        self.assertEqual(sorted_stack.pop(), 2)
        self.assertEqual(sorted_stack.pop(), 3)
        self.assertEqual(sorted_stack.pop(), 4)
        self.assertEqual(sorted_stack.pop(), 5)


if __name__ == 'main':
    unittest.main()
