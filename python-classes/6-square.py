#!/usr/bin/python3
"""A square based on the 5-square.py"""


class Square:
    """add a attribute to to give a position to the square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    """checks that size in a int above 0"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = value

    """checks that position is a tuple"""
    @position.setter
    def position(self, value):
        count = 0
        while 1:
            if type(value) != tuple or len(value) != 2:
                count += 1
                break
            if type(value[0]) != int or type(value[1]) != int:
                count += 1
                break
            if value[0] < 0 or value[1] < 0:
                count += 1
            break
        if count == 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """Return the area"""
    def area(self):
        return self.__size ** 2

    """print the square"""
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
