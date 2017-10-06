import unittest
from data_structures.questions.zero_matrix import zero_matrix


class TestZeroMatrix(unittest.TestCase):
    def test_zero_matrix(self):
        matrix = [[1, 2, 3, 4],
                  [5, 6, 0, 8],
                  [9, 1, 2, 3]]

        zeroed_matrix = [[1, 2, 0, 4],
                         [0, 0, 0, 0],
                         [9, 1, 0, 3]]

        zero_matrix(matrix)
        self.assertEqual(matrix, zeroed_matrix)

    def test_edge_cases(self):
        matrix = []
        zero_matrix(matrix)
        self.assertEqual(matrix, [])

        matrix = [[0, 0, 0]]
        zero_matrix(matrix)
        self.assertEqual(matrix, [0, 0, 0])


if __name__ == "__main__":
    unittest.main()
