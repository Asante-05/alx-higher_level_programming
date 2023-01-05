#!/usr/bin/python3
""" matrix multiplication module
execute: python3 -m doctest -v ./tests/100-matrix_mul.txt
"""


def matrix_mul(m_a, m_b):
    """ function to multiply two matrices
    Args:
        m_a(list): list containing list of nums
        m_b(list): list containing list of nums
    Returns: a matrix
    """

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for row in m_a:
        if not row:
            raise ValueError("m_a can't be empty")
        for element in row:
            if not element:
                raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_b:
        if not row:
            raise ValueError("m_b can't be empty")
        for element in row:
            if not element:
                raise ValueError("m_b can't be empty")


    if not all(isinstance(i, (int, float)) for row in m_a for i in row):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(i, (int, float)) for row in m_b for i in row):
        raise TypeError('m_b should contain only integers or floats')
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')


    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
     #Create a result matrix with the correct dimensions
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

     # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
