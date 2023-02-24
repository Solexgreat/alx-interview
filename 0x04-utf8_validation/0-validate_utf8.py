#!/usr/bin/python3
"""UTF-8"""


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding
    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    result = False
    for i in range(len(data)):
        num = str(bin(data[i])[2:])
        if len(num) <= 8:
            result = True
        else:
            result = False
            break
    return (result)
