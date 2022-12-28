#!/user/bin/python3
"""
addition function
execute: python3 -m doctest -v ./tests/0-add_integer.txt
to test program
"""


def add_integer(a, b=98):
    """
    function to add to integers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(int(a) + int(b))
