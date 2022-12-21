#!/usr/bin/python3
""" Defines class square """


class Square:
    """ represents a square """

    def __init__(self, size=0):
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
        """ Functiont to calculate the area of a square
        Return: the area of the square
        """
        return self.__size * self.__size
