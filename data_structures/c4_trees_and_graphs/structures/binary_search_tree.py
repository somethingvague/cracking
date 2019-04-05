"""Custom BST implementation

For any given node n: left descendants <= n < right descendants
"""
from data_structures.c4_trees_and_graphs.structures.binary_tree import TreeNode


class BinarySearchTree:
    def __init__(self, data):
        """
        Args:
            data: data to be inserted at the root of the tree
        """
        self.root = TreeNode(data)

    def insert(self, data):
        """
        Inserts the data and maintains the order property in the tree

        Args:
            data: data to be inserted in a Tree

        """
        self._insert_node(TreeNode(data), self.root)

    def insert_node(self, node):
        """
        Inserts the data and maintains the order property in the tree

        Args:
            node: node to be inserted in a Tree

        """
        self._insert_node(node, self.root)

    def _insert_node(self, node, from_node):
        """Helper for 'insert_node' method

        Args:
            node: node to be inserted in the tree
            from_node: a parent node which the data will be inserted under

        """
        if node.data <= from_node.data:
            if from_node.left is None:
                from_node.left = node
                node.parent = from_node
            else:
                self._insert_node(node, from_node.left)
        else:
            if from_node.right is None:
                from_node.right = node
                node.parent = from_node
            else:
                self._insert_node(node, from_node.right)

    def search(self, data):
        """Searches for a key in the tree from the root

        Args:
            data: data to search for in the tree

        Returns:
            True if the data is present in the tree, else False

        """
        return self._search(data, self.root)

    def _search(self, data, node):
        """

        Args:
            data: data to search for from the node
            node: node at which to search for data

        Returns:
            True if the node, or a descendant of the node, represents the data, else False

        """
        if node.data == data:
            return True
        elif data < node.data:
            return False if node.left is None else self._search(data, node.left)
        else:
            return False if node.right is None else self._search(data, node.right)
