#!/usr/bin/python3
"""
Module Matrix_divided
Divide a matrix
"""


def matrix_divided(matrix, div):
    """Returns a new matrix
    of results of a divided matrix
    """
    if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
        raise TypeError("Matrix must be a matrix (list of lists) of \
integers/floats")

    for a in matrix:
        if len(a) == 0:
            raise TypeError("Matrix must be a matrix (list of lists) of \
integers/floats")
        for b in a:
            if type(b) != int and type(b) != float:
                raise TypeError("Matrix must be a matrix (list of lists) of \
integers/floats")

    be = []
    for a in matrix:
        be.append(len(a))
    if not all(item == be[0] for item in be):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    ab = [[round(x / div, 2) for x in a] for a in matrix]

    return ab
