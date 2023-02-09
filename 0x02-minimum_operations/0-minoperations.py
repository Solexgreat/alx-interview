#!/usr/bin/python3
"""Return the minimum Operation used"""


def minOperations(n : int)-> int:
    """function calculate the minimum operation to get to (n)"""
    H : int = 1
    i : int = 0
    result = False
    if type(n) != int or n < 0 or n == 1:
        return (0)
    while H <= n:
        if H != 1 and n % H == 0 and H < n and H != n:
            H += 1
            result = True
            break
        H += 1
        result = False
    if result == False:
        return (0)    
    if result:
        H = 1
        while H < n:
            if H == 1 or n % H == 0:
                H *= 2
                i += 2
            else:
                H += H/2
                i += 1
        return(i)