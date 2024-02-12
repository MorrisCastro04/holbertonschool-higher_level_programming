#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """init te class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """set and get of width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    """set and get of height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    """set and get of x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    """set and get of y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
