#!/usr/bin/python3
""" module to modify text file
execute: ./100-main.py
require: a text file
"""


def append_after(filename="", search_string="", new_string=""):
    """ function to modify a text file
    Args:
        filename(string): file object
        search_string(string): string to search for
        new_string(string): string to insert
    """

    new_text = ""
    with open(filename) as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, "w") as w:
        w.write(new_text)
