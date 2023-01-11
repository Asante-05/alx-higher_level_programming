#!/usr/bin/python3
""" module containg json decoder
execute: ./4-main.oy
"""


import json


def from_json_string(my_str):
    """ functiont to dencode json
    Args:
        my_str(string): string object
    Return: string represented as a json file
    """
    return json.loads(my_str)
