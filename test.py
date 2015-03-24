#!/usr/bin/python

from mymodule import *
import sqlstuff

import unittest

class TestStringFunctions(unittest.TestCase):
    def testStringReversalWorksCorrectly(self):
        self.assertEqual(reverse('Hund'), 'dnuH')
        self.assertEqual(reverse('Marius Kleiner'), 'renielK suiraM')

    def testUpperCaseWorksCorrectly(self):
        self.assertEqual(uppercase('Marius'), 'MARIUS')
        self.assertEqual(uppercase('asdfs'), 'ASDFS')

    def testSaveAndRestorePersistentValue(self):
        sqlstuff.initialize()
        sqlstuff.storeAmount('Jesus', 1234)
        sqlstuff.storeAmount('Marius', -123)
        self.assertEqual(sqlstuff.loadAmount('Jesus'), 1234)
        self.assertEqual(sqlstuff.loadAmount('Marius'), -123)
        self.assertEqual(sqlstuff.loadAmount('Ndugu'), None)
        

if __name__ == '__main__':
    unittest.main()

