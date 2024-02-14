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
    @staticmethod
    def to_json_string(list_dictionaries):
        """checks if list_dict is not None"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    """json string to file"""
    @classmethod
    def save_to_file(cls, list_objs):
        """checks if list_objs is empty"""
        if list_objs is None:
            list_objs = []
        list_dict = []
        with open(cls.__name__ + ".json", 'w') as file:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
            str_obj = cls.to_json_string(list_dict)
            file.write(str_obj)

    """Json string to dictionary"""
    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)
