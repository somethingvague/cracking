"""Question 2.5
Write a function that sums 2 numbers represented by linked lists
"""

from data_structures.chapter_2.linked_list import Node


def _get_or_default(node):
    return Node(0) if node is None else node


def _sum_lists(first, second, carry):
    if first is None and second is None:
        return None

    first = _get_or_default(first)
    second = _get_or_default(second)
    value = carry + first.data + second.data
    portion = (value % 10)
    result = Node(portion)
    result.next = _sum_lists(first.next, second.next, value >= 10)
    return result


def sum_lists(first, second):
    return _sum_lists(first, second, 0)
