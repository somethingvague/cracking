"""Custom stack implementation"""
from data_structures.c3_stacks_and_queues.node import Node


class Stack:
    def __init__(self):
        self._top = None

    def pop(self):
        """Returns the data at the top of the stack and moves the top down one

        raises:
            IndexError if the stack is empty
        """
        self._raise_if_empty()
        item = self._top.data
        self._top = self._top.next
        return item

    def push(self, item):
        """Pushes a new node onto the stack

        Args:
            item: data to be wrapped in a node which will become the new top
        """
        node = Node(item)
        node.next = self._top
        self._top = node

    def peek(self):
        """Returns the data at the top of the stack without popping it off

        raises:
            IndexError if the stack is empty
        """
        self._raise_if_empty()
        return self._top.data

    def is_empty(self):
        """Returns true if there is no node on the top of the stack"""
        return self._top is None

    def _raise_if_empty(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
