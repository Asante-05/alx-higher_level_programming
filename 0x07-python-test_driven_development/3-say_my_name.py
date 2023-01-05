#!/usr/bin/python3
"""
module - contains funtion to print name
execute: python3 -m doctest -v ./tests/3-say_my_name.txt
"""


def say_my_name(first_name, last_name=""):
    """
    function to print full name
    Args:
        first_name(string): first argument to function
        second_name(string): second argument to unction
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(str("My name is {} {}".format(first_name, last_name)))
