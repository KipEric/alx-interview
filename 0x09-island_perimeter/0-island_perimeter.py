#!/usr/bin/python3
"""
a Python function that calculates the perimeter of
the island based on the provided grid
"""


def island_perimeter(grid):
    """A function that calculates the perimeter of
    the island based on the provided grid
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row-1][col] == 1:
                    perimeter -= 1
                if row < rows - 1 and grid[row+1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col-1] == 1:
                    perimeter -= 1
                if col < cols - 1 and grid[row][col+1] == 1:
                    perimeter -= 1

    return perimeter
