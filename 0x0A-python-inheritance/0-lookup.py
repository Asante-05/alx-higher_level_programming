#!/usr/bin/python3
""" module to containing one function
execite: ./0-main.py
"""


def lookup(obj):
    """ function to print all attributes and methods
        of an onject
    Args:
        obj(object) - argumnet ot function
    Return: list of all attributes and method
    """
    return dir(obj)
