#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []

    for i in matrix:
        x = list(map(lambda n: n ** 2, i))
        square_matrix.append(x)

    return (square_matrix)
