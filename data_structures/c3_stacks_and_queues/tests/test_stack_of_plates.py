import unittest

from data_structures.c3_stacks_and_queues.questions.stack_of_plates import SetOfStacks


class TestSetOfStacks(unittest.TestCase):
    def test_pop_raises_IndexError_when_no_stacks(self):
        with self.assertRaises(IndexError):
            SetOfStacks(4).pop()

    def test_push_adds_new_stack(self):
        stack_set = SetOfStacks(3)
        stack_set.push(1)
        self.assertEqual(len(stack_set.stacks), 1)

    def test_push_adds_new_stack_when_capacity_reached(self):
        stack_set = SetOfStacks(1)
        stack_set.push(1)
        stack_set.push(2)
        self.assertEqual(len(stack_set.stacks), 2)

    def test_pop_removes_stack_when_empty(self):
        stack_set = SetOfStacks(1)
        top_value = 2
        stack_set.push(1)
        stack_set.push(top_value)
        self.assertEqual(stack_set.pop(), top_value)
        stack_set.pop()
        self.assertEqual(len(stack_set.stacks), 1)

