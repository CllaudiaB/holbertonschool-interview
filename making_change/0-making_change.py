#!/usr/bin/python3
"""Make change"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
       determine the fewest number of coins needed
       to meet a given amount total"""

    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        count += total // coin
        total %= coin

    if total == 0:
        return count
    return -1
