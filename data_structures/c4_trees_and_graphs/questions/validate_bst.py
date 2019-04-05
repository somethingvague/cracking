"""Question 4.5

Implement a function to check whether a binary tree is a binary search tree
"""


def is_binary_search_tree(tree, min_data = None, max_data = None):
    """
    Args:
        tree: TreeNode to validate
        min_data: lower threshold to check
        max_data: higher threshold to check

    Returns:
        True if the tree is a binary search tree, else False

    """
    if tree is None:
        return True  # we have recursed to a leaf without violation

    if min_data is not None and tree.data < min_data or max_data is not None and tree.data > max_data:
        return False

    # Recurse left and right sub trees, updating the thresholds
    return is_binary_search_tree(tree.left, min_data, tree.data) and \
        is_binary_search_tree(tree.right, tree.data + 1, max_data)
