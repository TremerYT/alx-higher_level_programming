#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = []
    for column in matrix:
        result = list(map(lambda x: x**2, column))
        matrix_square.append(result)
    return matrix_square
