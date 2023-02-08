#!/usr/bin/python3
"""Return the minimum Operation used"""

def minOperations(n):
    """function calculate the minimum operation to get th arg(n)"""
    H = 1
    i = 0
    while H < n:
        if H == 1 or n % H == 0:
            H *= 2 
            i += 2
        else:
            H += H
            i += 1
    return i         