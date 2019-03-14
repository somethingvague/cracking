import unittest

from data_structures.c2_linked_lists.questions.sum_lists import sum_lists
from utils.utils import create_linked_list


class TestSumLists(unittest.TestCase):
    def test_sum_lists_of_equal_length(self):
        first = create_linked_list([7, 1, 6])
        second = create_linked_list([5, 9, 2])

        result = sum_lists(first, second)
        expected = create_linked_list([2, 1, 9])
        self.assertEqual(result, expected)

    def test_sum_lists_of_unequal_length(self):
        first = create_linked_list([7, 1])
        second = create_linked_list([5, 9, 2])

        result = sum_lists(first, second)
        expected = create_linked_list([2, 1, 3])
        self.assertEqual(result, expected)
