"""Expands docstring of a function. Used as decorator."""


import docstring_expander.constants as cn
from docstring_expander.kwarg import Kwarg

import typing


class Expander(object):

  def __init__(self, kwargs:typing.List[Kwarg],
       base:typing.List[str],
       includes:typing.List[str]=None,
       excludes:typing.List[str]=None,
       header:str="",
       trailer:str="",
       indent:int=4):
    """
    Parameters
    ----------
    kwargs: keyword arguments to document
    base: base list of arguments
    includes: additional arguments to include
    excludes: arguments to exclude
    header: header to print a beginning
    trailer to print at the end
    indent: spaces of indentiation
    """
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
    self.header = header
    self.trailer = trailer

  def _indentText(self, text, indent_str):
    strings = text.split("\n")
    textList= ["%s%s" % (indent_str, s) for s in strings]
    return '\n'.join(textList)

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
    indent_str = self._getIndentStr(indent)
    # Construct the expansion
    if len(self.header) > 0:
      expansion = self._indentText(self.header, indent_str)
    else:
      expansion = ""
    keywords = list(self.keywords)
    keywords.sort()
    for idx, keyword in enumerate(keywords):
      self.kwarg_dct[keyword].setIndent(self._indent)
      expansion += str(self.kwarg_dct[keyword])
    expansion += self._indentText(self.trailer, indent_str)
    # Replace the docstring
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
