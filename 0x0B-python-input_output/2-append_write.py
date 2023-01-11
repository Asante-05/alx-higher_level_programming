#!/usr/bin/python3
""" module to append to file
execute: ./2-main.py
"""


def append_write(filename="", text=""):
    """ functiont to append to file
    Args:
        filename(string): name of the file
        text: string to be written
    Return: number of characters written
    """

    count = 0
    with open(filename, mode="a", encoding="utf-8") as myfile:
        for char in text:
            myfile.write(char)
            count += 1
        return count
