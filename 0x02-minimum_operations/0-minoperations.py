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
    while i * i <= n:
        while n % i == 0:
            num_op += i
            n //= i
        i += 1
    if n > 1:
        num_op += n
    return num_op
