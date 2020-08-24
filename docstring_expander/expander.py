"""Expands docstring of a function. Used as decorator."""


import docstring_expander.constants as cn


class Expander(object):

  def __init__(kw_args, base, includes=None, excludes=None):
    self.base = base
    if includes is None:
      includes = []
    if excludes is None:
      excludes = []
    self.includes = includes
    self.excludes = excludes
    self.keywords = set(base).difference(excludes)
    self.keywords = list(self.keywords.union(includes))

  def __call__(self, func):
    string = func.__doc__
    pos = string.index(cn.EXPAND)
    if pos < 0:
        return func
    # Find the indentation for the line
    indent = pos
    for idx in range(1, pos):
      if string[pos - idx] != " ":
        indent = idx
        break
    # Construct the expansion
    expansion = ''.join([str(k) k in self.keywords])
    # Replace the docstring
    func.__doc__ = string.replace(cn.EXPAND, expansion)
    return func
      
    
