"""Question 2.4
Delete a node in the middle of a singly linked list, given only access to that node"""


def delete_middle_node(node):
    """Removes the a node from a linked list

    Args:
        node: the node to remove
    Returns:
        boolean representing success
    """
    if node is None or node.next is None:
        return False

    node.data = node.next.data
    node.next = node.next.next
    return True
