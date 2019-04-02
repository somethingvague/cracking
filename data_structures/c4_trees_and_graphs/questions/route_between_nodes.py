"""Question 4.1

Given a directed graph, implement an algorithm to determine whether there is a path between 2 nodes
"""
from data_structures.c4_trees_and_graphs.structures.graph import breadth_first_search, depth_first_search


def path_exists_dfs(from_node, to_node):
    """Determines whether the path exists using breadth first search
    Args:
        from_node: starting node
        to_node: target node

    Returns:
        True if there is a path connecting the nodes, else False

    """
    return depth_first_search(from_node, lambda node: node == to_node)


def path_exists_bfs(from_node, to_node):
    """Determines whether the path exists using breadth first search
    Args:
        from_node: starting node
        to_node: target node

    Returns:
        True if there is a path connecting the nodes, else False

    """
    return breadth_first_search(from_node, lambda node: node == to_node)
