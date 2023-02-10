#!/usr/bin/python3
"""Return the minimum Operation used"""


def minOperations(n):
    """function calculate the minimum operation to get to (n)"""


    if not isinstance(n, int) or n < 2:
        return (0)

    H = 1
    i = 0

    while H < n:
        rest = n - H
        if rest % H == 0:
            H *= 2
            i += 2
        else:
            H += H/2
            i += 1
    return (i)