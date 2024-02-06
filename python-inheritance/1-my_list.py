#!/usr/bin/python3
"""
    class that in inherits from list
"""


class MyList(list):
    """
        method to sort a list
    """
    def print_sorted(self):
        print(sorted(self))
