"""Contains classes to for a custom binary tree implementation"""


def visit(node):
    print(node.data, end=' ')


def in_order_traversal(node):
    """Traverses the tree recursively in order: left, current, right"""
    if node is not None:
        in_order_traversal(node.left)
        visit(node)
        in_order_traversal(node.right)


def pre_order_traversal(node):
    """Traverses the tree recursively in order: current, left, right"""
    if node is not None:
        visit(node)
        in_order_traversal(node.left)
        in_order_traversal(node.right)


def post_order_traversal(node):
    """Traverses the tree recursively in order: left, right, current"""
    if node is not None:
        in_order_traversal(node.left)
        in_order_traversal(node.right)
        visit(node)


class TreeNode:
    """Node with left and right children"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
