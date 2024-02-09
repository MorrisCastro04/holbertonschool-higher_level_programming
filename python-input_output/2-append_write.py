#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'wr+', encoding='utf-8') as file:
        file.seek(0, 2)
        file.write(text)
        file.seek(0)
        return len(text)
