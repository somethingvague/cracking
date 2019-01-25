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

    def append_to_tail(self, data):
        """Adds a node to the end of the linked list.

            Args:
                 data: data to be appended as a new node to the list.
        """
        node = self

        while node.next is not None:
            node = node.next

        node.next = Node(data)

    def delete_node(self, data):
        """Removes the first node containing data.

        Args:
            data: data to be removed from the list
        Raises:
            ValueError if the data is not in the list.
        """
        node = self

        if node.data == data:
            return node.next

        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
                return node

            node = node.next

        raise ValueError("{} not found".format(data))

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Node):
            return self.data == o.data
        return False

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    """Implementation of a singly-linked list with a head node."""

    def __init__(self, head_data=None):
        if head_data is not None:
            self.head = Node(head_data)
        else:
            self.head = None
