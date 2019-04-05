from nose.tools import assert_true, assert_false

from data_structures.c4_trees_and_graphs.questions.validate_bst import is_binary_search_tree
from data_structures.c4_trees_and_graphs.structures.binary_tree import TreeNode


def test_is_binary_search_tree_returns_true_given_valid_bst():
    bst = TreeNode(5)
    bst.left = TreeNode(3)
    bst.right = TreeNode(6)
    bst.left.left = TreeNode(2)
    bst.left.right = TreeNode(4)

    assert_true(is_binary_search_tree(bst))


def test_is_binary_search_tree_returns_false_given_invalid_bst():
    bst = TreeNode(5)
    bst.left = TreeNode(3)
    bst.right = TreeNode(6)
    bst.left.left = TreeNode(2)
    bst.left.right = TreeNode(40)  # This node violates the order property since it is greater than the root

    assert_false(is_binary_search_tree(bst))
