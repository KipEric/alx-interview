#!/usr/bin/python3
"""
A program that solves the N queens problem.
"""


import sys


def is_safe(board, row, col, N):
    """
    A function that checks if placing a queen at
    a given position on the board is safe according
    to the rules of the N queens problem.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def nqueens(board, row, N):
    """
    A function that tries to place queens in different columns,
    while respecting the constraints of the N queens problem.
    """
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            nqueens(board, row + 1, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1 for _ in range(N)]
    nqueens(board, 0, N)
