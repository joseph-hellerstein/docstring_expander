# Docstring Expander

This project addresses a common problem with the development of python packages in which there several higher level functions that have are many keyword options that are processed by low level functions. Typically, the higher level functions use `**kwargs` to pass keywords transparently to the lower level functions. This is an excellent use of python's capabilities.
But it creates a problem when used with intellisense in that the keyword options are only exposed at the lower level.

To illustrate, consider the following low level plotting function that is called by two plotting functions.

    
    def lowlevelPlot(data, num_col:int=2, num_row:int=3, bins=100):
        """
        General plot function.
     
        Parameters
        ----------
        num_col: Number of columns of plots
        num_row: Number of rows of plots
        bins: Number of bins
        """
        ...
    
    def plotHist(data:np.ndarray, num_col:int=2, num_row:int=3, bins=100): 
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
        lowlevelPlot(num_col=num_col, num_row=num_row, bins=bins)
     
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
         lowlevelPlot(num_col=num_col, num_row=num_row)
`

Since there is an almost unlimited number of options for plotting, we expect that the keyword options for ``genPlot`` will grow over time. For example, we may want to add options for a title, the position of the title, and its font. These should be transparently available to `hist` and `timeseries`, without changing their signatures or docstrings. So, a more maintainable version of these functions is:

    def plotHist(data, **kwargs):
        """
        Plot a histogram.
     
        Parameters
        ----------
        See lowlevelPlot.
        """
        ...
        lowlevelPlot(**kwargs)
        
    def plotTimeseries(data:np.ndarray, **kwargs):
        """
        Plot a histogram.
     
        Parameters
        ----------
        See lowlevelPlot.
        """
        ...
        lowlevelPlot(**kwargs)
    
But now intellisense doesn't work since the options exposed for a function by intellisese are what's in the docstring of function.

`docstring_expander` provides another solution. Suppose we have the following dictionary that describes all keyword arguments for `genPlot`:

    import docstring_expander as de
    
    kwargs = [
        de.Kwarg('num_col', dtype=int, default=2, doc='Number of columns of plots'),
        de.Kwarg('num_row', dtype=int, default=3, doc='Number of rows of plots'),
        de.Kwarg(name='bins' default=100, doc='Number of bins'),
        ]
 We define a few keyword arguments as common to most plotting functions.
 
    base = ['num_col', 'num_row']
    
Then we can write:
    
    @de.kwargs(kwargs, base, includes=['bins'])
    def plotHist(data:np.ndarray, **kwargs):
        """
        Plot a histogram.
     
        Parameters
        ----------
        #@expand
        """
        ...
        lowlevelPlot(**kwargs)
     
    @de.kwargs(kwargs, base)
    def plotTimeseries(data:np.ndarray, **kwargs):
        """
        Plot a histogram.
     
        Parameters
        ----------
        #@exapnd
        """
        ...
        lowlevelPlot(**kwargs)
    

For `plotHist`, the decorator replaces `#@expand` with:

        num_col: int
            Number of columns of plots
            default: 2
        num_row: int
            Number of rows of plots
            default: 3
        bins: 
            Number of bins
            default: 100
