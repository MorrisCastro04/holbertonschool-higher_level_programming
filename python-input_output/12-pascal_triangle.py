#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []
    pas = []
    for line in range(n):
        current = []
        for num in range(line + 1):
            if num == 0:
                current.append(1)
            elif num == line:
                current.append(1)
            else:
                current.append(pas[line - 1][num - 1] + pas[line - 1][num])
        pas.append(current)
    return pas
