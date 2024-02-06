#!/usr/bin/python3
"""
    return a booleant is exactly an instance
"""


def is_kind_of_class(obj, a_class):
    """
        check if the obj is the same type of a_class
    """
    if isinstance(obj, a_class):
        return True
    return False
