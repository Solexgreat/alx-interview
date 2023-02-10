#!/usr/bin/python3
"""Return the minimum Operation used"""


def minOperations(n):
    """function calculate the minimum operation to get to (n)"""
    if not isinstance(n, int) or n < 2:
        return (0)

    H = 1
    i = 0
    paste = 1
    while H < n:
        if n % H == 0:
            paste = H
            H *= 2
            i += 2
        else:
            H += paste
            i += 1
    return (i)
