import unittest

from data_structures.c2_linked_lists.questions.remove_dups import *
from utils.utils import random_integers, profile, create_linked_list


class TestRemoveDups(unittest.TestCase):
    def remove_dups(self, method):
        head = create_linked_list([1, 1, 2, 2, 3])

        method(head)

        self.assertEqual(head.data, 1)
        self.assertEqual(head.next.data, 2)
        self.assertEqual(head.next.next.data, 3)
        self.assertIsNone(head.next.next.next)

    def remove_dups_with_single_element(self, method):
        head = create_linked_list([1])

        method(head)

        self.assertEqual(head.data, 1)
        self.assertIsNone(head.next)

    def test_remove_dups_using_set(self):
        self.remove_dups(using_set)
        self.remove_dups_with_single_element(using_set)

    def test_remove_dups_using_pointers(self):
        self.remove_dups(using_pointers)
        self.remove_dups_with_single_element(using_pointers)

    def test_execution_times(self):
        integers = random_integers()
        head = create_linked_list(integers)
        profile("Remove dups using set", using_set, head)
        profile("Remove dups using pointers", using_pointers, head)

if __name__ == "__main__":
    unittest.main()
