# -*- coding: utf-8 -*-
"""
Created on Sunday August 23, 2020

@author: joseph-hellerstein
"""

from docstring_expander.expander import Expander
from docstring_expander.kwarg import Kwarg

import copy
import unittest


IGNORE_TEST = False
KWARGS = [
    Kwarg("num_col", default=3, doc="number of columns", dtype=int),
    Kwarg("num_row", default=3, doc="number of rows"),
    Kwarg("num_plot", doc="number of plots", dtype=int),
    Kwarg("plot_title", doc="Title of the plot", dtype=str),
    Kwarg("title_font", doc="Font size for plot", dtype=float),
    Kwarg("dummy"),
    ]
HEADER = """
Header line 1
Header line 2
"""
TRAILER = """
Trailer line 1
Trailer line 2
"""
BASE = ["num_row", "num_col", "title_font", "plot_title"]
DOCSTRING = """
  This is a test function.
  
  Parameters
  ----------
  #@expand
  """
    

def func(arg, **kwargs):
  """
  This is a test function.
  
  Parameters
  ----------
  #@expand
  """
  return kwargs.values()

@Expander(KWARGS, BASE)
def funcExpanded(arg, **kwargs):
  """
  This is a test function.
  
  Parameters
  ----------
  #@expand
  """
  return kwargs.values()
        

class TestExpander(unittest.TestCase):

  def setUp(self):
    self.expander = Expander(KWARGS, BASE)
    self.func = copy.deepcopy(func)
    self.func.__doc__ = DOCSTRING

  def testConstructor(self):
    if IGNORE_TEST:
      return
    diff = set(self.expander.keywords).symmetric_difference(BASE)
    self.assertEqual(len(diff), 0)

  def testCall(self):
    if IGNORE_TEST:
      return
    new_func = self.expander.__call__(self.func)
    for key in BASE:
      self.assertTrue(key in new_func.__doc__)

  def testCallHeader(self):
    if IGNORE_TEST:
      return
    expander = Expander(KWARGS, BASE, header=HEADER)
    new_func = expander.__call__(self.func)
    self.assertTrue("Header" in new_func.__doc__)

  def testCallTrailer(self):
    if IGNORE_TEST:
      return
    expander = Expander(KWARGS, BASE, trailer=TRAILER)
    new_func = expander.__call__(self.func)
    self.assertTrue("Trailer" in new_func.__doc__)

  def testDecorator(self):
    if IGNORE_TEST:
      return
    new_func = self.expander.__call__(self.func)
    self.assertTrue(new_func.__doc__, funcExpanded.__doc__)

  def construct(self, excludes=[], includes=[]):
    expander = Expander(KWARGS, BASE, excludes=excludes, includes=includes)
    new_func = expander.__call__(self.func)
    return new_func.__doc__

  def testExclude(self):
    if IGNORE_TEST:
      return
    #
    string = self.construct(excludes=BASE[1:])
    for key in BASE[1:]:
      self.assertFalse(key in string)

  def testInclude(self):
    if IGNORE_TEST:
      return
    string = self.construct(includes=["num_plot"])
    a_list = list(BASE)
    a_list.append("num_plot")
    for key in a_list:
      self.assertTrue(key in string)


if __name__ == '__main__':
    unittest.main()
