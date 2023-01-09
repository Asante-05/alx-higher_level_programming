#!/usr/bin/python3
""" module containing is_kind_of function
execute: ./3-main.py
"""


def is_kind_of_class(obj, a_class):
    """ function to check if obj belongs to a_class
    Args:
        obj: object
        a_class: class
    Return: True if obj belongs to class else false
    """
    return True if isinstance(obj, a_class) else False
