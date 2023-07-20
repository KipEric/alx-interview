#!/usr/bin/python3
"""
A script that find minimum number of operations
"""


def minOperations(n):
    """
    Function to find min operation required to reach H
    """
    if n <= 1:
        return 0
    num_op = 0
    i = 2
    while i <= n:
        if n % i == 0:
            num_op += i - 1
            n = n // i
            i -= 1
        i += 1
    return num_op
