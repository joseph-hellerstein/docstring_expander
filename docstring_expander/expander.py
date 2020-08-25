"""Expands docstring of a function. Used as decorator."""


import docstring_expander.constants as cn
from docstring_expander.kwarg import Kwarg

import typing


class Expander(object):

  def __init__(self, kwargs:typing.List[Kwarg],
       base:typing.List[str],
       includes:typing.List[str]=None,
       excludes:typing.List[str]=None,
       indent:int=4):
    self.kwarg_dct = {k.name: k for k in kwargs}
    self.base = base
    self._indent = indent
    if includes is None:
      includes = []
    if excludes is None:
      excludes = []
    self.includes = includes
    self.excludes = excludes
    self.keywords = set(base).difference(excludes)
    self.keywords = list(self.keywords.union(includes))

  def __call__(self, func:typing.Callable):
    string = func.__doc__
    pos = string.index(cn.EXPAND)
    if pos < 0:
        return func
    # Find the indentation for the line
    indent = pos
    for idx in range(1, pos):
      if string[pos - idx] != " ":
        indent = idx - 1
        break
    # Construct the expansion
    expansion = ""
    keywords = list(self.keywords)
    keywords.sort()
    for idx, keyword in enumerate(keywords):
      self.kwarg_dct[keyword].setIndent(self._indent)
      expansion += str(self.kwarg_dct[keyword])
    # Replace the docstring
    indent_str = self._getIndentStr(indent)
    replace_str = "%s%s"  % (indent_str, cn.EXPAND)
    func.__doc__ = string.replace(replace_str, expansion)
    return func

  def _getIndentStr(self, indent):
    return ''.join([" " for _ in range(indent)])

  def validate(self, kwargs:dict):
    """
    Validates the keyword arguments provided.
    """
    for key in kwargs.keys():
        self.assertTrue(key in self.kwarg_dct.keys())
        self.kwarg_dct[key].value().validate(kwargs[key])
