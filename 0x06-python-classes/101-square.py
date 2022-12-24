#!/usr/bin/python3
""" Defines class square """


class Square:
    """ represents a square """

    def __init__(self, size=0, position=(0, 0)) -> None:
        """ Inirializing a new square.
        Args:
            size(int): the size of the new square
            position(tuple): the position of the square
        """

        self.size = size
        self.position = position

    def __str__(self):
        """custom print output representation
        Args:
            self: object
        Returns: None
        """
        return self.my_print()[:-1]

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

    @property
    def position(self):
        """ Function to get the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Function to set the position
        Args:
            value(tuple): tuple containing the value for position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Function to print square
        """
        final = ""
        if self.__size == 0:
            final = "\n"
            return final
        else:
            for _ in range(self.position[1]):
                final += "\n"
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    final += " "
                for j in range(self.__size):
                    final += "#"
                final += "\n"
            return final
