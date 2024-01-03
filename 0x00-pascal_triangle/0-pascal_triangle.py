#!/usr/bin/python3

def pascal_triangle(n):
    """This function prints the pascal triangle"""
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        row = [1]
        prev_row = triangle[-1]

        for m in range(1, len(prev_row)):
            row.append(prev_row[m - 1] + prev_row[m])

        row.append(1)
        triangle.append(row)

    return triangle
