"""Question 4.2

Given a sorted array write an algorithm to create a BST with minimal height
"""
from data_structures.c4_trees_and_graphs.structures.binary_tree import TreeNode


def build_minimal_tree(arr):
    """Builds a tree of minimal height by recursively partitioning the array

    Args:
        arr: list from which to build the binary tree

    Returns:
        Binary Search Tree of minimal height
    """
    if len(arr) > 0:
        root_index = len(arr) // 2
        root = TreeNode(arr[root_index])
        root.left = build_minimal_tree(arr[: root_index])
        root.right = build_minimal_tree(arr[root_index + 1:])
        return root
    return None
