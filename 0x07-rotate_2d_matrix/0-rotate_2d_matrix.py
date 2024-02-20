#!/usr/bin/python3
"""This script rotate matrix"""


def rotate_2d_matrix(matrix):
    """This function reverses the matrix"""
    n = len(matrix)

    # transpose the matrix
    for k in range(n):
        for m in range(k + 1, n):
            matrix[k][m], matrix[m][k] = matrix[m][k], matrix[k][m]
    # this creates new matrix instead of updating the original maxtrix inplace
    # matrix = [[matrix[m][k] for m in range(n)] for k in range(n)]

    # reverse each row
    for k in range(n):
        matrix[k].reverse()
