#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """init the class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """getter from the attr size"""
    @property
    def size(self):
        return self.width

    """setter from the attr size"""
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """string method"""
    def __str__(self):
        """return the info of the class"""
        string = f"[Square] ({self.id})"
        string += f" {self.x}/{self.y} - {self.height}"
        return string
