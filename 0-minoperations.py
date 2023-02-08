def minOperations(n):
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