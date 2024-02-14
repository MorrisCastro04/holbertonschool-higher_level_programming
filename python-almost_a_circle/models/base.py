#!/usr/bin/python3
"""class base"""
import json


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

    """dict to json string"""
    def to_json_string(list_dictionaries):
        """checks if list_dict is not None"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
