import unittest

from data_structures.c2_linked_lists.questions.kth_to_last import kth_to_last
from utils.utils import create_linked_list


class TestKthToLast(unittest.TestCase):
    def test_returns_kth_to_last_node(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        node = kth_to_last(head, 2)
        self.assertEqual(node.data, 3)

        head.append_to_tail(9)
        node = kth_to_last(head, 2)
        self.assertEqual(node.data, 4)

if __name__ == "__main__":
    unittest.main()
