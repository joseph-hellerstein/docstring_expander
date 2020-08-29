"""Defines and validates a keyword argument."""


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
    self.dtype = dtype  # Data type
    self._indent = 0

  def setIndent(self, indent):
    self._indent = indent

  def getIndentStr(self):
    return ''.join([" " for _ in range(self._indent)])

  def __str__(self):
    """
    Creates a string representation of the Kwarg, properly indented.
    
    Returns
    -------
    str
    """
    def render(string):
      if string is None:
        return ""
      else:
        return string
    #
    indent_str = self.getIndentStr()
    stg = "%s%s: %s\n" % (indent_str, self.name, _prune(render(self.dtype)))
    if self.doc is not None:
      stg += "%s    %s\n" % (indent_str, render(self.doc))
    if self.default is not None: 
      stg += "%s    default = %s\n" % (indent_str, str(self.default))
    return stg

  def validate(self, value:object):
    """
    Checks the type of value for the keyword argument.

    Parameters
    ----------
    value: Checks type of value.   
    """
    if not isinstance(value, self.dtype):
        raise ValueError("Got type %s, but should be type %s"
            % (str(type(value)), str(type(self.dtype))))
