# Keyword Argument Manager

This project addresses a common problem with the development of python packages in which there several higher level functions that have are many keyword options that are processed by low level functions. Typically, the higher level functions use `**kwargs` to pass keywords transparently to the lower level functions. This is an excellent use of python's capabilities.
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

Since there is an almost unlimited number of options for plotting, we expect that the keyword options for ``genPlot`` will grow over time. For example, we may want to add options for a title, the position of the title, and its font. These should be transparently available to `hist` and `timeseries`, without changing their signatures or docstrings. So, a more maintainable version of these functions is:

    def plotHist(data, **kwargs):
        """
        Plot a histogram.
     
        Parameters
        ----------
        See genPlot.
        """
        ...
        
    def plotTimeseries(data:np.ndarray, **kwargs):
        """
        Plot a histogram.
     
        Parameters
        ----------
        See genPlot.
        """
        ...
    
However, this raises a secondary issue with intellisense since the options exposed for a function by intellisese are what's in the docstring of function. We could painfully repeat this information for each function, but this quickly becomes a maintenance nightmare.

`kwmgr` provides another solution. Suppose we have the following dictionary that describes all keyword arguments for `genPlot`:

    kwargs = {
        'num_col': (int, 2, 'Number of columns of plots'),
        'num_row': (int, 3, 'Number of rows of plots'),
        'bins': (int, 100, 'Number of bins'),
        }
 Of these, we define a few keyword arguments as common to most plotting functions.
 
    base = ['num_col', 'num_row']
    
Then we can write:

    @kwargs(kwargs, include=['bins'])
    def plotHist(data:np.ndarray):
        """
        Plot a histogram.
     
        Parameters
        ----------
        #@kwmgr: expand
        """
        ...
     
    @expand(base=base)
    def plotTimeseries(data:np.ndarray):
        """
        Plot a histogram.
     
        Parameters
        ----------
        #@kwmgr: exapnd
        """
        ...
    

For `plotHist`, the decorator does the following:
- Changes the function definition to `plotHist(data:np.ndarray, num_col:int=2, num_row:int=3, bins:int=100)`
- Replaces `#@kwmgr: expand with:

        num_col: Number of columns of plots
            default: 2
        num_row: Number of rows of plots
            default: 3
        bins: Number of bins
            default: 100
   
   
