"""Custom queue implementation"""
from data_structures.c3_stacks_and_queues.node import Node


class Queue():
    """Queue implemented via a linked list where the front is the head"""

    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        """Returns true if there is no node in the queue"""
        return self.front is None

    def add(self, data):
        """Adds new node containing data to the back of the queue

        Args:
            data: data to be wrapped in a Node and added
        """
        node = Node(data)

        if self.is_empty():
            self.front = node
            self.back = self.front
        else:
            self.back.next = node
            self.back = self.back.next

    def remove(self):
        """Remove node and returns data from the front of the queue

        Raises: IndexError
        """
        self._raise_if_empty()
        to_remove = self.front
        self.front = self.front.next
        return to_remove.data

    def peek(self):
        """Returns data from the front node without removing it

        Raises: IndexError
        """
        self._raise_if_empty()
        return self.front.data

    def _raise_if_empty(self):
        """Raises IndexError if queue is empty"""
        if self.is_empty():
            raise IndexError('Queue is empty')
