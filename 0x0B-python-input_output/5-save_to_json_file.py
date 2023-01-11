#!/usr/bin/python3
"""module
execute: ./5-main.py
"""


import json


def save_to_json_file(my_obj, filename):
    """ functiont to write to file using json representation
    Args:
        my_obj(string): object to be written
        filename; name of the file
    """

    with open(filename, mode="w") as myfile:
        json.dump(my_obj, myfile)
