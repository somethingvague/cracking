"""Question 2.1
Write code to remove duplicates from an unsorted linked list
"""


def using_set(node):
    """Removes duplicate nodes by building a set of values and re-pointing the next_node pointers. O(N) space and time

    Args:
        node: input Node
    Returns:
        node: with duplicates removed
    """

    all_data = set()
    previous = None
    while node is not None:
        if node.data in all_data:
            previous.next = node.next
        else:
            all_data.add(node.data)
            previous = node

        node = node.next

    return node


def using_pointers(node):
    """Removes duplicate nodes by using 2 pointers including a runner which re-assigns nodes. O(N^2) time

    Args:
        node: input Node
    Returns:
        node: with duplicates removed
    """

    while node is not None:
        runner = node

        while runner.next is not None:
            if runner.next.data == node.data:
                runner.next = runner.next.next
            else:
                runner = runner.next

        node = node.next
