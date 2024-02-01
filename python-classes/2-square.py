#!/usr/bin/python3
"""Make a square with a size and error checks"""


class Square():
    """Check if the size is a interger above 0"""

    def __init__(self, size=0):
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = size
