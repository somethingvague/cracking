"""Custom stack implementation"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self._top = None

    def pop(self):
        """Returns the data at the top of the stack and moves the top down one

        raises:
            IndexError if the stack is empty
        """
        self._raiseIfEmpty()
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
        self._raiseIfEmpty()
        return self._top.data

    def isEmpty(self):
        """Returns true if there is no node on the top of the stack"""
        return self._top is None

    def _raiseIfEmpty(self):
        if self.isEmpty():
            raise IndexError('Stack is empty')
