from nose.tools import assert_true, assert_false

from data_structures.c4_trees_and_graphs.questions.check_balanced import is_balanced
from data_structures.c4_trees_and_graphs.structures.binary_tree import TreeNode


def test_in_balance_returns_false_when_tree_not_balanced():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.right = TreeNode(6)

    assert_false(is_balanced(root))


def test_in_balanced_returns_true_when_tree_is_balanced():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right = TreeNode(6)

    assert_true(is_balanced(root))
