#!/usr/bin/python3
""" non empty class
execute: ./6-main.py
"""


class BaseGeometry:
    """ class containing one method """

    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")
