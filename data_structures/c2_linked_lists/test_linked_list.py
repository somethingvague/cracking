import unittest

from data_structures.c2_linked_lists.linked_list import Node


class TestNode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.node_1_data = 1
        cls.node_2_data = 2
        cls.node_3_data = 3

    def test_append_to_tail(self):
        head = Node(self.node_1_data)
        self.assertEqual(head.data, self.node_1_data)

        head.append_to_tail(self.node_2_data)
        self.assertEqual(head.next, Node(self.node_2_data))

        head.append_to_tail(self.node_3_data)
        self.assertEqual(head.next.next, Node(self.node_3_data))

    def test_delete_node_with_missing_data(self):
        with self.assertRaises(ValueError):
            head = Node("Some data")
            head.delete_node("Bob")

    def test_delete_node(self):
        head_data = "Some data"
        data_to_remove = "Some more data"
        tail_data = "Even more data"
        head = Node(head_data)
        head.append_to_tail(data_to_remove)
        head.append_to_tail(tail_data)

        new_head = head.delete_node(data_to_remove)

        self.assertEqual(new_head.data, head_data)
        self.assertEqual(new_head.next.data, tail_data)
        self.assertIsNone(new_head.next.next)


if __name__ == "main":
    unittest.main()
