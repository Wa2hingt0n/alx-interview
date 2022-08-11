#!/usr/bin/python3
""" Defines a function 'makeChange' """


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to meet a given
    amount total

    Args:
        coins: List of integers of the coins in possesion
        total: The amount to be met by coins

    Returns:
        - Fewest number of coins needed to meet 'total'
        - 0 if 'total' is 0 or less
        - -1 if total cannot be met by any number of coins in your possession
    """
    if total <= 0:
        return 0

    balance = total
    count = 0
    i = 0
    coin_list = sorted(coins, reverse=True)
    n = len(coins)
    while balance > 0:
        if i > n - 1:
            return -1
        if balance - coin_list[i] >= 0:
            balance -= coin_list[i]
            count += 1
        else:
            i += 1
    return count
