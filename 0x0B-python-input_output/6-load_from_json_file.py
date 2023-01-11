#!/usr/bin/python3
"""module
execute: ./6-main.py
"""


import json


def load_from_json_file(filename):
    """ functiont that creates an object from a json file
    Args:
        filename; name of the file
    """

    with open(filename) as myfile:
        return json.load(myfile)
