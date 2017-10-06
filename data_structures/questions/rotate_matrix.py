"""
Question 1.7
Rotate an image represented by an NxN matrix
"""
from math import floor


def rotate_matrix(matrix):
    """
    Rotates an NxN matrix 90 degrees clockwise in place in O(N^2)

    Args:
        matrix: NxN matrix
    Returns:
        Rotated matrix
    """

    # We only need to iterate half the number of layers the matrix has, doing so rotates the opposite layers
    for layer_idx in range(floor(len(matrix) / 2)):
        layer_length = len(matrix) - layer_idx
        for element_idx in range(layer_idx, layer_length - 1):
            # Save top value
            temp = matrix[layer_idx][element_idx]
            # Top = Left
            matrix[layer_idx][element_idx] = matrix[layer_length - element_idx - 1][layer_idx]
            # Left = Bottom
            matrix[layer_length - element_idx - 1][layer_idx] = matrix[layer_length - 1][layer_length - element_idx - 1]
            # Bottom = Right
            matrix[layer_length - 1][layer_length - element_idx - 1] = matrix[element_idx][layer_length - 1]
            # Right = Top (Saved)
            matrix[element_idx][layer_length - 1] = temp
