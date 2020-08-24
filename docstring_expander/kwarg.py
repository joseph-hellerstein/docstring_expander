"""Defines a keyword argument."""


class Kwarg(object):

  def __init__(self, name, default=None, doc=None, dtype=None):
    self.name = name  # Keyword
    self.default = default  # Default value of keyword
    self.doc = doc  # String to describe keyword
    self.dtype = dtype  # Data type

  def __str__(self):
        """
        Creates a string representation of the Kwarg.
        
        Returns
        -------
        str
        """
        pass
