import unittest
from data_structures.c3_stacks_and_queues.questions.stack_min import StackWithMin


class TestStackWithMin(unittest.TestCase):
    def test_pop_raises_error_when_stack_is_empty(self):
        stack = StackWithMin()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_push_and_pop(self):
        stack = StackWithMin()
        first_data = 2
        second_data = 4
        stack.push(first_data)
        stack.push(second_data)
        self.assertEqual(stack.pop(), second_data)
        self.assertEqual(stack.pop(), first_data)

    def test_min(self):
        stack = StackWithMin()
        stack.push(3)
        self.assertEqual(stack.min(), 3)

        stack.push(2)
        self.assertEqual(stack.min(), 2)

        stack.push(5)
        self.assertEqual(stack.min(), 2)

        stack.pop()
        stack.pop()
        self.assertEqual(stack.min(), 3)


if __name__ == 'main':
    unittest.main()