#!/usr/bin/python3
"""
    writes a string to a text file
"""


def write_file(filename="", text=""):
    """open a txt file and if not exist create it"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
