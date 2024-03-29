#!/usr/bin/python3
"""
    function that will add 2 integers.
    First number will be a and second number will be b.
    Return the addition of a and b.
"""


def add_integer(a, b=98):
    """
        Function that adds 2 integers.
        Check if a and b are integers or floats.
        If not a error will be raised.
        Otherwise float will be casted to integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
