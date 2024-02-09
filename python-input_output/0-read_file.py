#!/usr/bin/python3
"""
    Open a file UTF-8
"""


def read_file(filename=""):
    """open a file utf-8"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
