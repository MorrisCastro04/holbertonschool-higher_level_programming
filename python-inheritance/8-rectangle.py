#!/usr/bin/python3
"""
    a class named Rectangle
    pass a width and a height
"""


class Rectangle():
    """
        init the width and the height
    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        raise Exception("area() is not implemented")
