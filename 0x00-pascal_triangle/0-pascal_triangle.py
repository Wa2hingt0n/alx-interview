#!/usr/bin/python3
""" Contains a function `pascal_triangle(n)`"""


def pascal_triangle(n):
    """ Returns a list of lists representing the Pascal's triangle

        Args:
            n(int): Length of the Pascal's triangle
    """
    if n <= 0:
        return []
    triangle_list = []
    for i in range(1, n+1):
        c = 1
        coeff_list = []
        for j in range(1, i+1):
            coeff_list.append(c)
            c = int(c * (i - j) / j)
        triangle_list.append(coeff_list)

    return triangle_list
