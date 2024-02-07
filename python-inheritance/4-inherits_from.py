#!/usr/bin/python3
"""
    funcion that return boolean if the object is
    an instance of, or if the object is an instance of
    a class that inherited from, the specified class
"""


def inherits_from(obj, a_class):
    """
        check if obj is a instance
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
