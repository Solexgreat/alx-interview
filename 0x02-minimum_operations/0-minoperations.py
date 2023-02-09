#!/usr/bin/python3
"""Return the minimum Operation used"""


def minOperations(n):
    """function calculate the minimum operation to get to (n)"""
    H = 1
    i = 0
    result = False
    while H <= n:
        if H != 1 and n % H == 0 and H < n and H != n:
            H += 1
            result = True
            break
        H += 1
        result = False
    if result == False or type(n) == float or n < 0 or n == 1:
        return (0)
    H = 1     
    while H < n:
        if H == 1 or n % H == 0:
            H *= 2
            i += 2
        else:
            H += H/2
            i += 1
    return(i)