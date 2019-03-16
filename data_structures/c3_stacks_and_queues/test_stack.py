import unittest
from data_structures.c3_stacks_and_queues.stack import Stack


class TestStack(unittest.TestCase):
    def test_pop_raises_IndexError_when_stack_isEmpty(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_raises_IndexError_when_stack_isEmpty(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_push_pop_and_peek(self):
        stack = Stack()
        first_data = 2
        second_data = 5
        stack.push(first_data)
        stack.push(second_data)
        self.assertEqual(stack.peek(), second_data)

        popped = stack.pop()
        self.assertEquals(popped, second_data)
        self.assertEquals(stack.peek(), first_data)

        popped = stack.pop()
        self.assertEquals(popped, first_data)


if __name__ == "main":
    unittest.main()
