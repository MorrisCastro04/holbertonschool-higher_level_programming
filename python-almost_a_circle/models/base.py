#!/usr/bin/python3
"""class base"""


class Base():
    """private attribute"""
    __nb_objects = 0
    """init the class"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
