#!/usr/bin/python3
""" square module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ class xonstructor
        Args:
            size(int): private instance attribute
            x(int): private instance attribute
            y(int): private instance attribute
            id=None
        Raises:
            TypeError: if the arg value is not an int
            ValueError: if the value is invalid for the arg
        """

        super().__init__(size, size, x, y, id=None)
        """self.size = size"""

    @property
    def size(self):
        """ returns the size of the square instance """
        return self.width

    @size.setter
    def size(self, value):
        """ sets the value of the size of square """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method to reassign the args of rectangle instance
        Args:
            args(int): array of integers
            kwargs(dictionary): contains keys(argument names) and values
        """
        if args and len(args) != 0:
            arguments = []
            for item in args:
                arguments.append(item)
            if 0 < len(arguments):
                self.id = args[0]
            if 1 < len(arguments):
                self.size = args[1]
            if 2 < len(arguments):
                self.x = args[2]
            if 3 < len(arguments):
                self.y = args[3]
        else:
            for arg, value in kwargs.items():
                self.__setattr__(arg, value)

    def __str__(self):
        """ str method """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id,
                        self.x,
                        self.y,
                        self.size))

    def to_dictionary(self):
        """ fucntion to return the dictionary representation
            of t the class instance
        """
        return {'id': getattr(self, "id"),
                'x': getattr(self, "x"),
                'size': getattr(self, "size"),
                'y': getattr(self, "y")}
