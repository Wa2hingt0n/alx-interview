#!/usr/bin/python3
""" Algorithm for rotating a 2D matrix by 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """ Rotates a 2D matrix by 90 degrees clockwise """
    n = len(matrix)
    j = 0
    matrix_new = matrix.copy()
    while j < n:
        i = 1
        matrix[j] = []
        while i <= n:
            matrix[j].append(matrix_new[n - i][j])
            i += 1
        j += 1
