"""Question 2.6
Is the linked list a palindrome?
"""


def is_palindrome_with_list(node):
    """Determines whether the data in a linked list forms a palindrome.

    Implementation adds all node data to a list and then iterates from both sides, comparing the values.
    O(N) Space and Time

    Args:
        node: the node
    Returns:
        True if the list data is the same front-to-back and back-to-front
    """
    data_list = []
    while node is not None:
        data_list.append(node.data)
        node = node.next

    i = 0
    j = len(data_list)

    while i >= j:
        if data_list[i] != data_list[-i]:
            return False
        i += 1
        j -= 1

    return True


def is_palindrome_with_stack(node):
    """Determines whether the data in a linked list forms a palindrome.

    Implementation uses a stack to store the first half of the list and then pops off each item
    when comparing elements in the latter half. O(N) Space and Time

    Args:
        node: the node
    Return:
        True if the list data is the same front-to-back and back-to-front
    """
    data_stack = []

    # Advance a runner node twice as quickly so we know when to stop adding items to the stack and
    # when to start popping
    runner = node
    while runner is not None and runner.next is not None:
        data_stack.append(node.data)
        node = node.next
        runner = runner.next.next

    # handle uneven list sizes
    if runner is not None:
        node = node.next

    # pop the data off the stack and compare
    while node is not None:
        if node.data != data_stack.pop():
            return False
        node = node.next

    return True
