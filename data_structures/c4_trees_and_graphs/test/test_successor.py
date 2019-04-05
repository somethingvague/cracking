from nose.tools import assert_equal, assert_is_none

from data_structures.c4_trees_and_graphs.questions.successor import successor
from data_structures.c4_trees_and_graphs.structures.binary_search_tree import BinarySearchTree
from data_structures.c4_trees_and_graphs.structures.binary_tree import TreeNode


def test_successor_returns_successor_given_right_subtree_exists():
    bst = BinarySearchTree(5)
    bst.insert_node(TreeNode(8))
    bst.insert_node(TreeNode(7))
    successor_node = TreeNode(6)
    bst.insert_node(successor_node)

    assert_equal(successor(bst.root), successor_node)


def test_successor_returns_parent_given_no_right_sub_tree_exists_parent_on_right():
    bst = BinarySearchTree(5)
    bst.insert_node(TreeNode(3))
    parent = TreeNode(8)
    bst.insert_node(parent)
    from_node = TreeNode(7)
    bst.insert_node(from_node)
    bst.insert_node(TreeNode(9))

    assert_equal(successor(from_node), parent)


def test_successor_returns_next_parent_on_right_given_no_right_sub_tree_exists():
    bst = BinarySearchTree(5)
    successor_node = TreeNode(4)
    bst.insert_node(successor_node)
    bst.insert_node(TreeNode(2))
    from_node = TreeNode(3)
    bst.insert_node(from_node)

    assert_equal(successor(from_node), successor_node)


def test_successor_returns_none_given_leaf_of_right_most_branch():
    from_node = TreeNode(8)
    bst = BinarySearchTree(5)
    bst.insert_node(TreeNode(3))
    bst.insert_node(TreeNode(7))
    bst.insert_node(TreeNode(6))
    bst.insert_node(from_node)

    assert_is_none(successor(from_node))
