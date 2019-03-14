import unittest

from data_structures.c2_linked_lists.questions.partition import partition
from utils.utils import create_linked_list


class TestPartition(unittest.TestCase):
    def test_partition(self):
        head = create_linked_list([3, 5, 8, 5, 10, 2, 1])
        result = partition(head, 5)
        expected = create_linked_list([1, 2, 3, 5, 8, 5, 10])
        self.assertEqual(result, expected)
