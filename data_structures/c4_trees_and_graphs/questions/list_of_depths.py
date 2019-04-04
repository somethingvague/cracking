"""Question 4.3

Given a binary tree, return lists containing the nodes at each level
"""


def _build_list_of_depths(node, depths, level):
    """Adds the node to the depths structure

    Args:
        node: the TreeNode to record
        depths: the list to which we're populating
        level: the level of the node in the tree

    """
    if node is None:
        return

    # initialise the level if needed
    if len(depths) == level:
        depths.append([])

    depths[level].append(node)
    _build_list_of_depths(node.left, depths, level + 1)
    _build_list_of_depths(node.right, depths, level + 1)


def list_of_depths(tree):
    """
    Args:
        tree: TreeNote from which to construct the list of linked lists

    Returns:
        A list of lists representing the nodes at each level
        e.g. index 0 contains the root only, index 1 contains the immediate children etc.

    """
    depths = []
    _build_list_of_depths(tree, depths, 0)
    return depths

