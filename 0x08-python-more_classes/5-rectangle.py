#!/usr/bin/python3
""" module for rectangle class
execute: ./3-main.py
"""


class Rectangle:
    """ rectangle class
    contains getter and mutator methods
    """

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ returns the area of a rectangle instance """
    def area(self):
        return self.__height * self.__width

    """ returns the perimter of a rectange instance """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    """ str implementation to return rectange instace """
    def __str__(self):
        if (self.__height != 0 and self.__width != 0):
            x = self.__width * '#' + '\n'
            y = ""
            for i in range(self.__height):
                if i == self.height - 1:
                    y += self.__width * '#'
                else:
                    y += x
            return y
        else:
            return ("")

    """ repr """
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """ del """
    def __del__(self):
        print("Bye rectangle...")
