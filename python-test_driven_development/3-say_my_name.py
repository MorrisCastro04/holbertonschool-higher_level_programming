#!/usr/bin/python3
"""
    funcion to print a full name
"""


def say_my_name(first_name, last_name=""):
    """
    prints the formated string 'my name is <first_name> <last_name>'
    Args: first_name(str), last_name(str, optional)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
