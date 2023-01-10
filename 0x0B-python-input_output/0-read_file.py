#!/usr/bin/python3
""" module to read file
execute: ./0-main.py
"""


def read_file(filename=""):
    """ functiont to read from a file
    Args:
        filename(string): name of the file
    """

    with open(filename, encoding="utf-8") as myfile:
        for line in myfile:
            print(line, end="")
