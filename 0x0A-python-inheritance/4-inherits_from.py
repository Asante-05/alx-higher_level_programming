#!/usr/bin/python3
""" module containing is_kind_of function
execute: ./4-main.py
"""


def inherits_from(obj, a_class):
    """ function to check if obj inherits from a_class
    Args:
        obj: object
        a_class: class
    Return: True if obj is an instance of a_class else false
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
