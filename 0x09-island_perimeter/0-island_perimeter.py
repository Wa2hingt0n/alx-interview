#!/usr/bin/python3
""" Defines a function 'island_perimeter' """


def island_perimeter(grid):
    """ Returns the perimeter of the island described in 'grid'

    Args:
        grid: List of list of integers, where 1 is land and 0 is water. each
        cell is a square of length 1
    """
    perimeter = 0
    c = 0
    r = 0
    if grid:
        rows = len(grid)
        columns = len(grid[0])
        while r < rows:
            c = 0
            while c < columns:
                if r < rows and c < columns and grid[r][c] == 1:
                    cell_perimeter = 4
                    if c + 1 < columns and grid[r][c + 1] == 1:
                        cell_perimeter -= 1
                    if r + 1 < rows and grid[r + 1][c] == 1:
                        cell_perimeter -= 1
                    if c != 0 and grid[r][c - 1] == 1:
                        cell_perimeter -= 1
                    if r != 0 and grid[r - 1][c] == 1:
                        cell_perimeter -= 1
                    perimeter += cell_perimeter
                c += 1
            r += 1
    return perimeter
