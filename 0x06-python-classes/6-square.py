#!/usr/bin/python3
""" Defines class square """


class Square:
    """ represents a square """

    def __init__(self, size=0, position=(0, 0)):
        """ Inirializing a new square.
        Args:
            size(int): the size of the new square
            position(tuple): the position of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

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
        self.__position = position

    def my_print(self):
        """ Function to print square
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for q in range(self.__position[0]):
                    print("{}".format(" "), end="")
                for j in range(self.__size):
                    print("{}".format("#"), end="")
                print("")
