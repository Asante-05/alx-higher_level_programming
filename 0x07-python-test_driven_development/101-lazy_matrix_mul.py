""" module for multiplying matrices with numpy
execute: python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt 
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ functiont to multiply two matrices
    Args:
        m_a(array): first arg to function
        m_b(array): second arg to function
    Return: an array
    """
    if type(m_a) not in [list, np.ndarray]:
        raise TypeError('m_a must be a matrix')
    if type(m_b) not in [list, np.ndarray]:
        raise TypeError('m_b must be a matrix')
    return np.dot(m_a, m_b)
