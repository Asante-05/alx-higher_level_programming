#!/usr/bin/python3
""" module containing a class
execute:
./1-main.py
python -m doctest -v 1-my_list.txt
"""


class MyList(list):
    """ class inheriting from list """

    def print_sorted(self):
        """ function to print sorted members of a list
            in ascending order
        Return: None
       """

        print(sorted(self))
