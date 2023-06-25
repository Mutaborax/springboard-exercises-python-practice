def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    diagonal_sum = 0
    for i in range(len(matrix)):
        # add to sum of top-left to bottom-right diagonal
        diagonal_sum += matrix[i][i]
        # add to sum of bottom-left to top-right diagonal
        diagonal_sum += matrix[i][len(matrix)-1-i]
    return diagonal_sum
