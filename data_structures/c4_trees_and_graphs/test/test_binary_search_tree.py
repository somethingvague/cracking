from nose.tools import assert_equal, assert_true, assert_false
from data_structures.c4_trees_and_graphs.structures.binary_search_tree import BinarySearchTree


class TestBinarySearchTree:
    def setup(self):
        self.bst = BinarySearchTree(5)
        self.bst.insert(3)
        self.bst.insert(8)
        self.bst.insert(4)

    def test_insert_maintains_node_order(self):
        assert_equal(self.bst.root.data, 5)
        assert_equal(self.bst.root.left.data, 3)
        assert_equal(self.bst.root.left.right.data, 4)
        assert_equal(self.bst.root.right.data, 8)

    def test_search_returns_true_when_data_present(self):
        assert_true(self.bst.search(4))

    def test_search_returns_false_when_data_present(self):
        assert_false(self.bst.search(42))
