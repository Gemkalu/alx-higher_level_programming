#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for a in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, a)))
    return new_matrix
