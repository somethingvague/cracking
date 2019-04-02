"""Custom Graph implemented as an adjacency list"""
from data_structures.c3_stacks_and_queues.queue import Queue


def breadth_first_search(node, matches):
    """Iteratively searches the graph by exploring each neighbour before moving to the next level

    Args:
        node: the starting node
        matches: function returning true if a given

    Returns:
        True if the node can be reached from the root, False otherwise

    """
    node.visited = True
    search_queue = Queue()
    search_queue.add(node)

    while not search_queue.is_empty():
        node = search_queue.remove()
        if matches(node):
            return True

        for child in node.children:
            if not child.visited:
                search_queue.add(child)
                child.visited = True

    return False


def depth_first_search(node, matches):
    """Recursively searches the graph by exploring each path fully before moving to the next

    Args:
        node: the starting node
        matches: function returning true if a given

    Returns:
        True if the node can be reached from the root, False otherwise

    """
    node.visited = True
    if matches(node):
        return True

    for child in node.children:
        if not child.visited and depth_first_search(child, matches):
            return True

    return False


class Graph:
    """Graph implementation with set of nodes which are not necessarily all connected

    Args:
        nodes: nodes to be stored in the graph

    """
    def __init__(self, nodes):
        self.nodes = nodes

    class Node:
        """Node to be used in a Graph

        Args:
            data: some data representing the node
            children: other nodes where the there are edges connecting from self

        Attributes:
            visited: denotes whether the node has already been visited in a search

        """
        def __init__(self, data, children):
            self.data = data
            self.children = children
            self.visited = False
