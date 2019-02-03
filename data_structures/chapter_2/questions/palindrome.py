"""Question 2.6
Is the linked list a palindrome?
"""


def is_palindrome_with_list(node):
    """Returns whether the data in a linked list forms a palindrome. O(N) Space and Time"""
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
    """Returns whether the data in a linked list forms a palindrome. O(N) Space and Time"""
    data_stack = []

    runner = node
    while runner is not None and runner.next is not None:
        data_stack.append(node.data)
        node = node.next
        runner = runner.next.next

    if runner is not None:
        node = node.next

    while node is not None:
        if node.data != data_stack.pop():
            return False
        node = node.next

    return True
