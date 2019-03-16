import unittest
from data_structures.c3_stacks_and_queues.questions.three_in_one import ThreeInOne


class TestThreeInOne(unittest.TestCase):
    def test_peek_raises_IndexError_when_stack_is_empty(self):
        three_in_one = ThreeInOne(3)
        with self.assertRaises(IndexError):
            three_in_one.peek(0)

    def test_push_raises_IndexError_when_stack_is_full(self):
        three_in_one = ThreeInOne(2)
        three_in_one.push(0, 1)
        three_in_one.push(0, 2)
        with self.assertRaises(IndexError):
            three_in_one.push(0, 3)

    def test_is_empty(self):
        three_in_one = ThreeInOne(3)
        three_in_one.push(0, 4)
        self.assertFalse(three_in_one.is_empty(0))
        self.assertTrue(three_in_one.is_empty(1))
        self.assertTrue(three_in_one.is_empty(2))

    def test_push_pop_peek(self):
        three_in_one = ThreeInOne(2)
        three_in_one.push(0, 1)
        three_in_one.push(0, 2)
        three_in_one.push(1, 3)
        three_in_one.push(2, 5)
        self.assertEqual(three_in_one.pop(0), 2)
        self.assertEqual(three_in_one.peek(0), 1)
        self.assertEqual(three_in_one.peek(2), 5)


if __name__ == 'main':
    unittest.main()
