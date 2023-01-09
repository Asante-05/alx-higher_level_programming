#!/usr/bin/python3
""" non empty class
execute:
./7-main.py
python -m doctest -v test/7-base_geometry.txt
"""


class BaseGeometry:
    """ class containing one method """

    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ methods to validate value
        Args:
            name(string): first argument
            value(int): second argument
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
