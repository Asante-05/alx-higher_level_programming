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
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for element in matrix:
        new_matrix.append(round(element / div, 2))
