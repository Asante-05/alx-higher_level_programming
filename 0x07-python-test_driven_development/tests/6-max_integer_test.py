#!/usr/bin/python3
""" Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_None(self):
        self.assertIsNone(max_integer([]))

    def test_output(self):

        """ ends with the max """
        self.assertEqual(max_integer([8, 0, 7, 32]), 32)

        """ begins with the max """
        self.assertEqual(max_integer([99, 98, 97, 96, 95]), 99)

        """ contains one negavite number """
        self.assertEqual(max_integer([99, -99]), 99)

        """ contains only negative numbers """
        self.assertEqual(max_integer([-99, -6, -1, -29, -3]), -1)

        """ contains float """
        self.assertEqual(max_integer([1, 1.2, 1.3, 1.5, 1.7, 1.9]), 1.9)

        """ contains only one number(+) """
        self.assertEqual(max_integer([5]), 5)

        """ contains only one number(-) """
        self.assertEqual(max_integer([-6]), -6)

        """ contains only one number(0) """
        self.assertEqual(max_integer([0]), 0)

        """ empty list """
        self.assertEqual(max_integer([]), None)

    def test_value(self):
        """ list contains a string """
        self.assertRaises(ValueError, max_integer, [2, -1, 'string', 10, 20])

        """ list contains a boolean """
        self.assertRaises(ValueError, max_integer, [2, True, 2010, 10, 20])

        """ list contains only strings """
        self.assertRaises(ValueError, max_integer,
                          ['my', 'name', 'is', 'software', 'dev'])

        """ list contains only chars """
        self.assertRaises(ValueError, max_integer, ['b', 'a', 'c', 'e', 'd'])

    def test_type(self):
        """ argument to function is of type 'tuple' """
        self.assertRaises(TypeError, max_integer, (2, -1, 4, 10, 20))

        """ argument to function is of type 'dictionary' """
        self.assertRaises(TypeError, max_integer,
                          {2: [2, 4, 6, 8], 1: [1, 2, 3, 4]})

        """ argument to function is of type 'boolean' """
        self.assertRaises(TypeError, max_integer, True)

        """ argument to function is of type 'integer' """
        self.assertRaises(TypeError, max_integer, 3)

        """ argument to function is of type 'char' """
        self.assertRaises(TypeError, max_integer, 'a')

        """ argument to function is of type 'string' """
        self.assertRaises(TypeError, max_integer, "any")
