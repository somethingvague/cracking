from nose.tools import assert_equal, assert_is_none
from data_structures.c4_trees_and_graphs.questions.minimal_tree import build_minimal_tree


def test_build_minimal_tree_with_even_number_of_elements():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bst = build_minimal_tree(arr)

    # Level 1
    assert_equal(bst.data, 6)

    # Level 2
    assert_equal(bst.left.data, 3)
    assert_equal(bst.right.data, 9)

    # Level 3
    assert_equal(bst.left.left.data, 2)
    assert_equal(bst.left.right.data, 5)
    assert_equal(bst.right.left.data, 8)
    assert_equal(bst.right.right.data, 10)

    # Level 4
    assert_equal(bst.left.left.left.data, 1)
    assert_equal(bst.left.right.left.data, 4)
    assert_equal(bst.right.left.left.data, 7)


def test_build_minimal_tree_with_odd_number_of_elements():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bst = build_minimal_tree(arr)

    # Level 1
    assert_equal(bst.data, 5)

    # Level 2
    assert_equal(bst.left.data, 3)
    assert_equal(bst.right.data, 8)

    # Level 3
    assert_equal(bst.left.left.data, 2)
    assert_equal(bst.left.right.data, 4)
    assert_equal(bst.right.left.data, 7)
    assert_equal(bst.right.right.data, 9)

    # Level 4
    assert_equal(bst.left.left.left.data, 1)
    assert_equal(bst.right.left.left.data, 6)
