#!/usr/bin/python3
"""
    from JSON to python
"""
import json


def from_json_string(my_str):
    """return my_str like a Object"""
    return json.loads(my_str)
