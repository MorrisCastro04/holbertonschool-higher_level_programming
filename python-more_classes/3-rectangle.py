#!/usr/bin/python3
"""
    a class of a rectangle
    have a height and a width
    height and width needs to be int
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

    """looks for the area of the rectangle"""
    def area(self):
        return self.__height * self.__width

    """looks for the perimeter of the rectangle"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    """print the rectangle"""
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        print_rect = ""
        for i in range(self.__height):
            for y in range(self.__width):
                print_rect += "#"
            if i is not self.__height - 1:
                print_rect += "\n"
        return print_rect
