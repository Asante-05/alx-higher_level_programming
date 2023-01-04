#!/usr/bin/python3
""" module for rectangle class
execute: ./8-main.py
"""


class Rectangle:
    """ rectangle class
    contains getter and mutator methods
    """
    number_of_instances = 0
    print_symbol = '#'

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

        Rectangle.number_of_instances += 1

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
            x = self.__width * '{0!s}'.format(self.print_symbol) + '\n'
            y = ""
            for i in range(self.__height):
                if i == self.height - 1:
                    y += self.__width * '{0!s}'.format(self.print_symbol)
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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """ compares two rectangles
    Args:
        rect_1(Rectangle): first argument
        rect_2(Rectangle): second argument
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
