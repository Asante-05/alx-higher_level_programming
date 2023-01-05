#!/usr/bin/python3
""" moduel to print a square
execute: python3 -m doctest -v ./tests/4-print_square.txt
"""


def print_square(size):
    """ function to print square with '#'
    Args:
        size(int): size of square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("{}".format('#'), end="")
        print()
