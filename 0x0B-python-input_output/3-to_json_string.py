#!/usr/bin/python3
""" module containg json encoder
execute: ./3-main.oy
"""


import json


def to_json_string(my_obj):
    """ functiont to encode json
    Args:
        myobj(object): json object
    Return: json representation of object
    """
    return json.dumps(my_obj)
