#!/usr/bin/python3
""" module to print text with separations 
execute: python3 -m doctest -v ./tests/5-text_indentation.txt
"""

def text_indentation(text):
    """ function to seperate text
    Args:
        text(string): text to be separated
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if i in ['.', ':', '?']:
                print(i)
                print()
                flag = 0
            else:
                print(i, end='')
