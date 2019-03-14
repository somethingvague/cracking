import unittest

from data_structures.c2_linked_lists.questions.delete_middle_node import delete_middle_node
from utils.utils import create_linked_list


class TestKthToLast(unittest.TestCase):
    def test_delete_middle_node(self):
        head = create_linked_list([1, 2, 3, 4, 5])

        self.assertTrue(delete_middle_node(head.next.next))
        self.assertEqual(head, create_linked_list([1, 2, 4, 5]))

        self.assertTrue(delete_middle_node(head.next))
        self.assertEqual(head, create_linked_list([1, 4, 5]))

        self.assertFalse(delete_middle_node(head.next.next))
