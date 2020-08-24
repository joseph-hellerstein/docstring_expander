# -*- coding: utf-8 -*-
"""
Created on Sunday August 23, 2020

@author: joseph-hellerstein
"""

from docstring_expander.kwarg import Kwarg

import unittest


IGNORE_TEST = True
IS_PLOT = True
NAME = "bins"
DOC = "Documentation for bins"
DTYPE = int
DEFAULT = 100
        

class TestKwarg(unittest.TestCase):

  def setUp(self):
    self.kwarg = Kwarg(NAME, doc=DOC, dtype=DTYPE,
        default=DEFAULT)

  def testConstructor(self):
    if IGNORE_TEST:
      return
    self.assertEqual(self.kwarg.name, NAME)

  def testStr(self):
    if IGNORE_TEST:
      return
    self.kwarg.setIndent(4)
    stg = str(self.kwarg)
    self.assertTrue(NAME in stg)
    self.assertTrue(DOC in stg)
    self.assertTrue("int" in stg)
    self.assertTrue(str(DEFAULT) in stg)

  def testValidate(self):
        # TESTING
    self.kwarg.validate(3)
    with self.assertRaises(ValueError):
        self.kwarg.validate('dummy')



if __name__ == '__main__':
    unittest.main()
