#!/usr/bin/python3
"""This script solves the N queens problem"""
import sys


def is_safe(board, row, col, n):
    """Cheching if there any queen in the some column"""
    for k in range(row):
        if board[k] == col or \
            board[k] - k == col - row or \
            board[k] + k == col + row:
                return False
    return True

def solve_nqueens_util(board, row, n, solutions):
    """checking all cells """
    if row == n:
        solutions.append([[k, board[k]] for k in range(n)])
    else:
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                solve_nqueens_util(board, row + 1, n, solutions)

def solve_nqueens(n):
    """This function start the game"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    
    solve_nqueens_util(board, 0, n, solutions)
    print(len(solutions))
    print()
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
        
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
