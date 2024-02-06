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

def solve_nqueens_util(board, row, n, solutions, memo):
    """checking all cells """
    if row == n:
        solutions.append([[k, board[k]] for k in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            memo[row][col] = True
            solve_nqueens_util(board, row + 1, n, solutions, memo)
            memo[row][col] = False

def solve_nqueens(n):
    """This function start the game"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    memo = [[False] * n for _ in range(n)]
    for l in memo:
        print(l)
    print()
    solve_nqueens_util(board, 0, n, solutions, memo)

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
