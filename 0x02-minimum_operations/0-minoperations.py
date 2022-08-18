#!/usr/bin/python3
""" Defines a function 'minOperations(n)' """
from math import sqrt


def minOperations(n):
    """ Calculates the fewest number of operations needed to result in exactly
    'n' 'H' characters in the file
    """
    if n == 0 or n == 1:
        return 0
    prime_factors = []
    num = n
    while num % 2 == 0:
        prime_factors.append(2)
        num /= 2

    for i in range(3, int(sqrt(num)) + 1, 2):
        while (num % i == 0):
            prime_factors.append(i)
            num = num / i

    if num > 2:
        prime_factors.append(int(num))

    return sum(prime_factors)
