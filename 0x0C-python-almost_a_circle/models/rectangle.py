#!/usr/bin/python3
""" rectangle module
"""

from models.base import Base
"""
Base = __import__("./base").Base
"""


class Rectangle(Base):
    """ public setters and getter for all private instance attributes """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor
        Args:
            width(int): private instance attribute
            height(int): private instance attribute
            x(int): private instance attribute
            y(int): private instance attribute
            id=None
        Raises:
            TypeError: if the arg value is not an int
            ValueError: if the value is invalid for the arg
        """
        if id is None:
            super().__init__(id=None)
        else:
            self.id = id

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        area: function to calculate the area of the rectangle instance
        Returns: the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """ function to print the rectangle in stdout
        """
        x = " " * self.x + self.__width * '#' + '\n'
        y = ""
        z = "" + '\n' * self.y
        y += z
        for row in range(self.__height):
            if row == self.__height - 1:
                y += " " * self.x + self.__width * '#'
            else:
                y += x
        print(y)

    def __str__(self):
        """ overiding the str magice method
        Return: the parameters passed to rectangle instance
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id,
                        self.__x,
                        self.__y,
                        self.__width,
                        self.__height))

    def update(self, *args, **kwargs):
        """ method to reassign the args of rectangle instance
        Args:
            args(int): array of integers
            kwargs(dictionary): contains keys(argument names) and values
        """
        """
        if len(args) == 0:
            for arg, value in kwargs.items():
                self.__setattr__(arg, value)
        """

        if args and len(args) != 0:
            arguments = []
            for item in args:
                arguments.append(item)
            if 0 < len(arguments):
                self.id = args[0]
            if 1 < len(arguments):
                self.__width = args[1]
            if 2 < len(arguments):
                self.__height = args[2]
            if 3 < len(arguments):
                self.__x = args[3]
            if 4 < len(arguments):
                self.__y = args[4]
        else:
            for arg, value in kwargs.items():
                self.__setattr__(arg, value)

    def to_dictionary(self):
        """ method to return a dictionary representation of
            class instance
        """
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
