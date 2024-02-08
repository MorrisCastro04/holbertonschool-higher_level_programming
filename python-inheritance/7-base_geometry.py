#!/usr/bin/python3
"""
    a class named BaseGeometry
    check name and value
"""


class BaseGeometry():
    """
        funcion that validate value
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
    """
        class with a public instance method
    """
    def area(self):
        raise Exception("area() is not implemented")
