#!/usr/bin/python3
""" defines class square """


class Square:
    """ represents a square """

    def __init__(self, size=None):
        """ Inirializing a new square.
        Args:
            size(int): the size of the new square
        """

        self._size = size
