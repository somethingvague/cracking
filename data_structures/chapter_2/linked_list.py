"""Contains custom linked list implementation for use in chapter_2 questions"""

class Node:
    """Singly-linked node which has data and a reference to the next node."""

    def __init__(self, data):
        """Initialises a node.

            Args:
                 data: the data encapsulated in the node
        """
        self.data = data
        self.next = None

    def __eq__(self, other):
        """Override default equals to compare value equality."""
        if isinstance(other, self.__class__):
            return other.__dict__ == self.__dict__

        return False


class LinkedList:
    """Implementation of a singly-linked list with a head node."""

    def __init__(self, head_data=None):
        if head_data is not None:
            self.head = Node(head_data)
        else:
            self.head = None

    def append_to_tail(self, data):
        """Adds a node to the end of the linked list.

            Args:
                 data: data to be appended as a new node to the list.
        """
        node = self.head

        if node is None:
            self.head = Node(data)
            return

        while node.next is not None:
            node = node.next

        node.next = Node(data)

    def delete_node(self, data):
        """Removes the first node containing data.

        :param data: data to be removed from the list
        :raises ValueError if the data is not in the list.
        """
        node = self.head

        if node.data == data:
            self.head = node.next
            return

        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
                return

            node = node.next

        raise ValueError("{} not found in list".format(data))
