# Docstring Expander

This project addresses a common problem with the development of python packages in which there are many keyword options that are processed by low level logic. This is an excellent use of python's capabilities.
But it creates a problem when used with intellisense in that the keyword options are only exposed at the lower level.

To illustrate, consider the following two functions intended as a high level plotting interface:

``def hist(data, num_col=2, num_row=3, bins=100):
  ...
  
``def timeseriesPlot(data, num_col-2, num_row=3):
  ...
 ``
