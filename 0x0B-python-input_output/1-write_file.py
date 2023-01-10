#!/usr/bin/python3
""" module to write file
execute: ./1-main.py
"""


def write_file(filename="", text=""):
    """ functiont to write string to a text file
    Args:
        filename(string): name of the file
        text: string to be written
    Return: number of characters written
    """

    count = 0
    with open(filename, mode="w", encoding="utf-8") as myfile:
        for char in text:
            myfile.write(char)
            count += 1
        return count
