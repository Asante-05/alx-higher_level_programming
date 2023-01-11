#!/usr/bin/python3
import json
""" module containg json encoder
execute: ./3-main.oy
"""


def to_json_string(my_obj):
    """ functiont to encode json
    Args:
        myobj(object): json object
    """
    return (json.dumps(my_obj))
