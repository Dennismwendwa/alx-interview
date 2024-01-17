#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """This method finds the minimum operations"""
    if n <= 1:
        return 0

    result = 0

    for k in range(2, int(n**0.5) + 1):
        while n % k == 0:
            result += k
            n //= k
    if n > 1:
        result += n

    return result
