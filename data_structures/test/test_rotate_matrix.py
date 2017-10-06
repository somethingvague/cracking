import unittest
from data_structures.questions.rotate_matrix import rotate_matrix


class TestRotateMatrix(unittest.TestCase):
    def test_odd_length_matrix_rotation(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        rotated = [[7, 4, 1],
                   [8, 5, 2],
                   [9, 6, 3]]

        rotate_matrix(matrix)
        self.assertEqual(matrix, rotated)

    def test_even_length_matrix_rotation(self):
        matrix = [[1, 2],
                  [3, 4]]

        rotated = [[3, 1],
                   [4, 2]]

        rotate_matrix(matrix)
        self.assertEqual(matrix, rotated)

    def test_edge_cases(self):
        single_element_matrix = [[1]]
        rotated_single_element_matrix = [[1]]
        rotate_matrix(single_element_matrix)
        self.assertEqual(single_element_matrix, rotated_single_element_matrix)

        empty_matrix = []
        rotate_matrix(empty_matrix)
        self.assertEqual(empty_matrix, [])

if __name__ == "__main__":
    unittest.main()
