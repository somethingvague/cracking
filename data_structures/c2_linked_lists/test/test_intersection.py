import unittest

from data_structures.c2_linked_lists.linked_list import Node
from data_structures.c2_linked_lists.questions.intersection import intersection_using_set, iterative_intersection
from utils.utils import create_linked_list


def append_node_to_tail(node, node_to_append):
    while node.next is not None:
        node = node.next

    node.next = node_to_append


class TestIntersection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create distinct first and second lists
        cls.first = create_linked_list([1, 2, 3, 4])
        cls.second = create_linked_list([11, 12])

        # append the intersecting node to the lists
        cls.intersecting_node = Node(5)
        append_node_to_tail(cls.first, cls.intersecting_node)
        append_node_to_tail(cls.second, cls.intersecting_node)

        # append some values to the intersecting node
        cls.intersecting_node.append_to_tail(8)
        cls.intersecting_node.append_to_tail(55)

    def test_intersection_using_hash(self):
        result = intersection_using_set(self.first, self.second)
        self.assertEqual(result, self.intersecting_node)

    def test_iterative_intersection(self):
        result = iterative_intersection(self.first, self.second)
        self.assertEqual(result, self.intersecting_node)
