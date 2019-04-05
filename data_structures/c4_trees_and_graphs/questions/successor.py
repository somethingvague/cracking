"""Question 4.6

Write an algorithm to find the "next" node in a binary search tree
"""


def _get_min(tree):
    """
    Args:
        tree: TreeNode from which to find the minimum node

    Returns:
        the node with the minimum data in the tress
    """
    return tree if tree.left is None else _get_min(tree.left)


def successor(node):
    """Gets the node in the tree with the next largest value

    Args:
        node: TreeNode to find the successor of

    Returns:
        Successor node if it exists, else None
    """
    data = node.data

    if node.right:
        return _get_min(node.right)  # get minimum value from the right sub tree

    # traverse up until the node we have is on the left of the parent
    while node is not None:
        if node.parent is not None and node.parent.data > data:
            return node.parent

        node = node.parent

    return node
