#!/usr/bin/python3
# Write a function that computes the square value of all integers of a matrix using mapdef square_matrix_map(matrix)

def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
