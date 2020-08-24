"""Defines a keyword argument."""


############# FUNCTIONS ############
def _prune(dtype):
  HEAD_STR = "<class '"
  TAIL_STR = "'>"
  stg = str(dtype)
  if HEAD_STR in stg:
    stg = stg.replace(HEAD_STR, '')
  if TAIL_STR in stg:
    stg = stg.replace(TAIL_STR, '')
  return stg


############# CLASSES ############
class Kwarg(object):

  def __init__(self, name, default=None, doc=None, dtype=None):
    self.name = name  # Keyword
    self.default = default  # Default value of keyword
    self.doc = doc  # String to describe keyword
    if dtype is None:
      dtype = ""
    else:
      dtype = str(dtype)
    self.dtype = dtype  # Data type
    self._indent = None

  def setIndent(self, indent):
    self._indent = indent

  def __str__(self):
    """
    Creates a string representation of the Kwarg, properly indented.
    
    Returns
    -------
    str
    """
    indent_str = ''.join([" " for _ in range(self._indent)])
    stg = "%s%s: %s\n" % (indent_str, self.name, _prune(self.dtype))
    if self.doc is not None:
      stg += "%s    %s\n" % (indent_str, self.doc)
    if self.default is not None: 
      stg += "%s    default = %s\n" % (indent_str, str(self.default))
    return stg
