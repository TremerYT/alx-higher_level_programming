#!/usr/bin/python3
"""This function defines the sum of two integers"""

def add_integer(a, b=98):
    """
    This adds two integers
    """

    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    try:
        a = int(a)
    except ValueError:
        raise TypeError("a mus be an integer")
    try:
        b = int(b)
    except ValueError:
        raise TypeError("b must be an integer")
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return a + b
