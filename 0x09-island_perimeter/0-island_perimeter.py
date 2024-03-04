#!/usr/bin/python3
"""This scripts find the area of any island"""


def island_perimeter(grid):
    """This function finds the area of the island"""

    perimeter = 0
    for k in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[k][c] == 1:
                if k == 0 or grid[k - 1][c] == 0:
                    perimeter += 1
                if k == len(grid) - 1 or grid[k + 1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[k][c - 1] == 0:
                    perimeter += 1
                if c == len(grid[0]) - 1 or grid[k][c + 1] == 0:
                    perimeter += 1

    return perimeter
