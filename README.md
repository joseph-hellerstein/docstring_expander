# Docstring Expander

This project addresses a common problem with the development of python packages in which there are many keyword options that are processed by low level logic. This is an excellent use of python's capabilities.
But it creates a problem when used with intellisense in that the keyword options are only exposed at the lower level.

To illustrate, consider the following two functions intended as a high level plotting interface:

``def plotHist(data, num_col=2, num_row=3, bins=100):``
  
``def plotTimeseries(data, num_col-2, num_row=3):``

Both of these functions call:

``def genPlot(data, num_col=2, num_row=3, bins=100):``

Since there are an almost unlimited number of options for plotting, we expect that the keyword options for ``genPlot`` will grow over time. Further these should be transparently available to ``hist`` and ``timeseries``. So, a more maintainable version of these functions would be:
``def plotHist(data, **kwargs):`` and ``def plotTimeseries(data, **kwargs):``.
However, this raises a secondary issue with intellisense since the options exposed are only those in the docstring of the function called. One solution is to repeat these options in each docstring, but this increases the maintenance burden.

`docstring-expander` provides another solution.
