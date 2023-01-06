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

    string = text[:]

    for c in ".?:":
        list_text = string.strip(c)
        string = ""
        for i in list_text:
            i = i.strip(" ")
            string = i + c if string is "" else string + "\n\n" + i + c
    print(string[:-3], end="")
