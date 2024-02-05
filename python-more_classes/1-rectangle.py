#!/usr/bin/python3
"""
    add the attributes heigth and width
"""


class Rectangle():
    """init the rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """getter for the width"""
    @property
    def width(self):
        return self.__width

    """getter for the height"""
    @property
    def height(self):
        return self.__height

    """setter of the width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """setter of the height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
