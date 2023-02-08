#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n):
    if n <= 0:
        return 0
    i = 2
    operations = 0
    while i <= n:
        while n % i == 0:
            operations += 1
            n /= i
        i += 1
    return operations + n
