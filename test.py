#!/usr/bin/python

from mymodule import *
import unittest

class TestStringFunctions(unittest.TestCase):
    def testStringReversalWorksCorrectly(self):
        self.assertEqual(reverse('Hund'), 'dnuH')
        self.assertEqual(reverse('Marius Kleiner'), 'renielK suiraM')

    def testUpperCaseWorksCorrectly(self):
        self.assertEqual(uppercase('Marius'), 'MARIUS')
        self.assertEqual(uppercase('asdfs'), 'ASDFS')

if __name__ == '__main__':
    unittest.main()

