#!/usr/bin/python3
"""load from a Json file"""
import json


def load_from_json_file(filename):
    """open a file"""
    with open(filename) as file:
        return json.load(file)
