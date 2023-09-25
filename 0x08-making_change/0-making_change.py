#!/usr/bin/python3
"""
A script to determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    function to determine the fewest number of
    coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        while total >= coin:
            num_coins += 1
            total -= coin
    if total != 0:
        return -1
    return num_coins
