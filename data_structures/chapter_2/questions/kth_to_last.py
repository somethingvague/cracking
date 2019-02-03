"""Question 2.2

Find the kth to last element in a singly linked list
"""


def kth_to_last(head, k):
    """Finds the kth to last node in a linked list

    Args:
        head: node in the linked list
        k: index from last to return
    Returns:
        Node kth to last node
    """
    runner = head
    node = head

    runner_count = 0
    while runner.next is not None:
        runner = runner.next
        runner_count += 1
        if runner_count > k:
            node = node.next

    return node
