#!/usr/bin/python3
"""
    funcion that return a boolean
"""


def is_same_class(obj, a_class):
    """
        check if the obj is the same type of a_class
    """
    if type(obj) is a_class:
        return True
    return False
