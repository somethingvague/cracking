"""Question 1.8
Given an NxM matrix, write a function which sets all values in the rows and columns to 0 where
there is a 0 in that column
"""


def zero_matrix(matrix):
    """Sets all values in columns and rows to 0 in place where there is an existing 0 in O(N^2)

    Args:
        matrix: NxM matrix
    """

    rows = set()
    columns = set()

    number_of_columns = len(matrix[0])
    number_of_rows = len(matrix)

    # Store row and column indexes which we need to 0
    for row_idx in range(number_of_rows):
        for col_idx in range(number_of_columns):
            if matrix[row_idx][col_idx] == 0:
                rows.add(row_idx)
                columns.add(col_idx)

    # 0 the rows then columns
    for row_idx in rows:
        for col_idx in range(number_of_columns):
            matrix[row_idx][col_idx] = 0

    for col_idx in columns:
        for row_idx in range(number_of_rows):
            matrix[row_idx][col_idx] = 0
