#!/usr/bin/python3
"""A square based on the 5-square.py"""


class Square():
    """add a attribute to to give a position to the square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = value

    def position(self, value):
        if type(value) is not tuple:
            print("position must be a tuple of 2 positive integers")
            raise TypeError

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1] > 0):
                    print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end='')
                print()
