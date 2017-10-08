import unittest
from data_structures.chapter_2.linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.node_1_data = 1
        cls.node_2_data = 2
        cls.node_3_data = 3

    def test_append_to_tail(self):
        # Append to empty list
        list = LinkedList()
        head = Node(self.node_1_data)

        list.append_to_tail(self.node_1_data)
        self.assertEqual(list.head, head)

        list = LinkedList(self.node_1_data)
        self.assertEqual(list.head, head)

        list.append_to_tail(self.node_2_data)
        self.assertEqual(list.head.next, Node(self.node_2_data))

        list.append_to_tail(self.node_3_data)
        self.assertEqual(list.head.next.next, Node(self.node_3_data))

if __name__ == "main":
    unittest.main()
