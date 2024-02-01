#!/usr/bin/python3
"""A square based on the 2-square.py"""


class Square():
    """Add a public method called area(self)"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = value

    def area(self):
        return self.__size ** 2
