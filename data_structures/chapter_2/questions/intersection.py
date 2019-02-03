"""Question 2.7
Given 2 linked lists determine if the 2 lists intersect by reference and return the reference
"""


def intersection_using_set(first, second):
    """Returns the first node that intersects 2 linked lists by reference

    Adds each node ID from one list into a set then iterates the other list comparing IDs.
    Time O(A+B), Space O(B)

    Args:
        first: a Node
        second: another Node
    Returns:
        the intersecting node, if it exists, else None
    """
    second_node_ids = set()
    while second is not None:
        second_node_ids.add(id(second))
        second = second.next

    while first is not None:
        if id(first) in second_node_ids:
            return first

        first = first.next

    return None


def _get_tail_and_size(node):
    """Returns the tail node and size of a linked list

    Args:
        node
    Returns:
        a tuple of node and size
    """
    size = 0
    while node is not None:
        size += 1
        node = node.next

    return node, size


def _strip_lists_to_equal_length(first, first_size, second, second_size):
    """Advances the largest list until they both have equal length

    Args:
        first: a node in a linked list
        first_size: length of the first list
        second: a node in a linked list
        second_size: length of the second list
    Returns:
        a tuple where the lengths are of equal size
    """
    if first_size == second_size:
        return first, second

    largest, smallest = first, second if first_size > second_size else (second, first)
    number_to_advance_largest_by = abs(first_size - second_size)
    while number_to_advance_largest_by > 0:
        number_to_advance_largest_by -= 1
        largest = largest.next

    return largest, smallest


def iterative_intersection(first, second):
    """Returns the first node that intersects 2 linked lists by reference

    Determines if an intersection exists, then evens up the list lengths and iteratively compares the nodes.
    Time O(A+B), Space O(1)

    Args:
        first: a Node
        second: another Node
    Returns:
        the intersecting node, if it exists, else None
    """
    first_tail_and_size = _get_tail_and_size(first)
    second_tail_and_size = _get_tail_and_size(second)

    # Check if tail is the same, if not there is no intersection
    if id(first_tail_and_size[0]) != id(second_tail_and_size[0]):
        return None

    # Make the lists of equal length and then compare the lists node by node
    first, second = _strip_lists_to_equal_length(first, first_tail_and_size[1], second, second_tail_and_size[1])
    while id(first) != id(second):
        first = first.next
        second = second.next

    return first
