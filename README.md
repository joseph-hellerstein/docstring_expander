# Keyword Argument Manager

This project addresses a common problem with the development of python packages in which there are many keyword options that are processed by low level logic. This is an excellent use of python's capabilities.
But it creates a problem when used with intellisense in that the keyword options are only exposed at the lower level.

To illustrate, consider the following two functions intended as a high level plotting interface:

    def plotHist(data:np.ndarray, num_col:int=2, num_row:int=3, bins:int=100): 
        """
        Plot a histogram.
     
        Parameters
        ----------
        num_col: Number of columns of plots
            default: 2
        num_row: Number of rows of plots
            default: 3
        bins: Number of bins
            default: 100
        """
        ...
     
     def plotTimeseries(data:np.ndarray, num_col:int=2, num_row:int=3):
         """
         Plot a histogram.
     
         Parameters
         ----------
         num_col: Number of columns of plots
            default: 2
         num_row: Number of rows of plots
         """
         ...
`

Both of these functions call:

    def genPlot(data, num_col:int=2, num_row:int=3, bins:int=100):
        """
        General plot function.
     
        Parameters
        ----------
        num_col: Number of columns of plots
        num_row: Number of rows of plots
        bins: Number of bins
        """
        ...

Since there are an almost unlimited number of options for plotting, we expect that the keyword options for ``genPlot`` will grow over time. Further these should be transparently available to ``hist`` and ``timeseries``. So, a more maintainable version of these functions would be:

    def plotHist(data, **kwargs):
        """
        Plot a histogram.
     
        Parameters
        ----------
        See genPlot.
        """
        ...
        
    def plotTimeseries(data:np.ndarray, num_col:int=2, num_row:int=3):
        """
        Plot a histogram.
     
        Parameters
        ----------
        See genPlot.
        """
        ...
    
However, this raises a secondary issue with intellisense since the options exposed are only those in the docstring of the function called. One solution is to repeat these options in each docstring, but this increases the maintenance burden.

`docstring-expander` provides another solution. Suppose we have the following dictionary that describes all keyword arguments to `genPlot`:

    kwargs = {
        'num_col': ('Number of columns of plots', 2),
        'num_row': ('Number of rows of plots', 3),
        'bins': ('Number of bins', 100),
        }
    base = ['num_col', 'num_row']
    
Then we can write:

    @expand(base=base, include='bins')
    def plotHist(data, **kwargs):
        """
        Plot a histogram.
     
        Parameters
        ----------
        #@expand
        """
        ...
     
    @expand(base=base)
    def plotTimeseries(data:np.ndarray, num_col:int=2, num_row:int=3):
        """
        Plot a histogram.
     
        Parameters
        ----------
        #@expand
        """
        ...
    

This replaces `#@expand` in `plotHist` with:
   
   
