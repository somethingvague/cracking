"""Question 4.4.

Given a tree check that the heights of the branches are balanaced (they differ no more than 1)
"""


def get_tree_height(tree):
    """
    Args:
        tree: the tree to get the height of

    Returns:
        The maximum height of the left and right sub trees

    """
    if tree is None:
        return -1

    return max(get_tree_height(tree.left), get_tree_height(tree.right)) + 1


def is_balanced(node):
    """
    Args:
        node: node to for which to check whether descendants are balanced or not

    Returns:
        True if the tree is balanced, else False

    """
    if node is None:
        return True

    left_height = get_tree_height(node.left)
    right_height = get_tree_height(node.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)
