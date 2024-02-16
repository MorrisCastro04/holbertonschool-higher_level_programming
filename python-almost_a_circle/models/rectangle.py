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

    """getter of width"""
    @property
    def width(self):
        return self.__width

    """setter of width"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """getter of height"""
    @property
    def height(self):
        return self.__height

    """setter of heigth"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """getter of x"""
    @property
    def x(self):
        return self.__x

    """setter of x"""
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """getter of y"""
    @property
    def y(self):
        return self.__y

    """setter of y"""
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """return the area of the circle"""
    def area(self):
        """height time width"""
        return self.__height * self.__width

    """display the rectangle"""
    def display(self):
        """run in each line to print # times the width"""
        i = 0
        while i < self.__y:
            print("")
            i += 1
        for line in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    """str method"""
    def __str__(self):
        """return the info of the class"""
        string = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        string += f" - {self.__width}/{self.__height}"
        return string

    """update the class rectangle"""
    def update(self, *args, **kwargs):
        """checks if the class have a atribute"""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) == 5:
            self.__y == args[4]

    """convert to dictionary"""
    def to_dictionary(self):
        """create the dictionary"""
        new_dict = {'x': self.__x, 'width': self.__width, 'id': self.id,
                    'height': self.__height, 'y': self.__y}
        return new_dict
