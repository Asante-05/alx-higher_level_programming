#!/usr/bin/python3
""" Inherits from BasicGeometry
execute: ./8-main.py
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ class defining Rectange using basic geometry """

    def __init__(self, width, height):
        """ initializing a new rectange """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
