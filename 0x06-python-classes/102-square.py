#!/usr/bin/python3
""" Defines class square """


class Square:
    """ represents a square """

    def __init__(self, size=0) -> None:
        """ Inirializing a new square.
        Args:
            size(int): the size of the new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Function to calculate the area of a square
        Return: the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ Functiont to retrieve the size of the square
        Return: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Function to set the size of the square
        Args:
            value(int): the new size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __le__(self, other):
        """less than or equal"""
        return self.area() <= other.area()

    def __ge__(self, other):
        """greater than or equal"""
        return self.area() >= other.area()

    def __ne__(self, other):
        """not equal"""
        return self.area() != other.area()

    def __gt__(self, other):
        """greater than"""
        return self.area() > other.area()

    def __lt__(self, other):
        """less than"""
        return self.area() < other.area()

    def __eq__(self, other):
        """equal"""
        return self.area() == other.area()
