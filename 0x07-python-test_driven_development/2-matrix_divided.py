#!/usr/bin/python3
""" module for dividing elements in a matrixe by div
execute: python3 -m doctest -v ./tests/2-matrix_divided.txt
"""


def matrix_divided(matrix, div):
    """ function to divide all elemts in a matrix
    Arges:
         matrix(list): matrix to be divided
         div(int/float): divisor
    """

    typeErr = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not isinstance(matrix, list):
        raise TypeError(typeErr)

    len_m = 0
    sizeErr = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(typeErr)

        if len_m != 0 and len(elements) != len_m:
            raise TypeError(sizeErr)

        for num in elements:
            if not type(num) in [int, float]:
                raise TypeError(typeErr)

        len_m = len(elements)

    mx = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (mx)
