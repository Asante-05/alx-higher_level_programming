#!/usr/bin/python3
""" module
execute: ./8-main.py
"""


def class_to_json(obj):
    """ defines a class to function 
    Args:
        obj(class): onject to be defined
    Returns: __dict__ for obj
    """

    return obj.__dict__
