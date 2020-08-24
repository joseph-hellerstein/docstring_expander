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
    self.keyworks = list(self.keywords.union(includes))

  # TODO: finish
  def __call__(self, func):
    pos = func.__doc__.index(cn.EXPAND)
    if pos < 0:
        return func
    else:
        # Find the indentation for the line
