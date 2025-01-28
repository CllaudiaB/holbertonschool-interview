#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
       determine the fewest number of coins needed
       to meet a given amount total"""

    if total <= 0:
        return 0
    else:
        c = 0
        sum_coins = sum(coins)
        diff = total - sum_coins
        if diff < 0:
            return -1
        while diff > 0:
            _min = min(coins)
            diff -= _min
            temp_diff = diff
            if diff in coins:
                diff = temp_diff
                break
            c += 1
        return c + 1
