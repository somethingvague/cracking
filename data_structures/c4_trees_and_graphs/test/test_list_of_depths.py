from nose.tools import assert_equal

from data_structures.c4_trees_and_graphs.questions.list_of_depths import list_of_depths
from data_structures.c4_trees_and_graphs.structures.binary_tree import TreeNode


def test_list_of_depths_returns_populates_correctly_from_stick_tree():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(2)
    root.left.left.left.left = TreeNode(1)

    result = list_of_depths(root)
    expected = [
        [root],
        [root.left],
        [root.left.left],
        [root.left.left.left],
        [root.left.left.left.left]
    ]

    assert_equal(result, expected)


def test_list_of_depths_populates_from_multi_level_tree():
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(6)

    result = list_of_depths(root)
    expected = [
        [root],
        [root.left, root.right],
        [root.left.left, root.left.right],
        [root.left.right.right],
    ]

    assert_equal(result, expected)
