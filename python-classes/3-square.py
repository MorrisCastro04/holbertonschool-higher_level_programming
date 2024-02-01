#!/usr/bin/python3
"""A square based on the 2-square.py"""


class Square():
    """Add a public method called area(self)"""

    def __init__(self, size=0):
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = size

    def area(self):
        return self.__size ** 2
