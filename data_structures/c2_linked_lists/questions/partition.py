"""Question 2.4
Partition a linked list around a value x such that all the nodes less than x come
"""


def partition(node, partition_value):
    """Partitions a linked list on a value by moving elements to elements to the head or tail

    Args:
        node: head of linked list
        partition_value: value on which to partition the linked list
    Returns:
        the partitioned linked list
    """
    head = node
    tail = node
    while node is not None:
        next = node.next
        if node.data < partition_value:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next

    tail.next = None
    return head
