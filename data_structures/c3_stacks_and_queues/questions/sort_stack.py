"""Question 3.5

Sort a stack so that the minimum is on top, can only use another stack as a data structure
"""
from data_structures.c3_stacks_and_queues.stack import Stack


def sort_stack(stack):
    """Sorts a stack by shuffling between 2 stacks

    Args:
        stack: stack to be sorted
    """
    s1 = stack
    s2 = Stack()
    while not s1.is_empty():
        item = s1.pop()
        # Pop items off the s2 so that the item from s1 can be inserted in the right place
        while not s2.is_empty() and s2.peek() < item:
            s1.push(s2.pop())
        s2.push(item)

    return s2
