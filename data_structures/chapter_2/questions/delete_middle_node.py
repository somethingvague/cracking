"""Question 2.4
Delete a node in the middle of a singly linked list, given only access to that node"""


def delete_middle_node(node):
    while node.next is not None:
        node.data = node.next.data
        node = node.next
