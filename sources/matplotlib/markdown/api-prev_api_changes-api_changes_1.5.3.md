[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.3.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

API Changes in 1.5.3[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.3.html#api-changes-in-1-5-3 "Link to this heading")

===============================================================================================================================================

`ax.plot(..., marker=None)` gives default marker[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.3.html#ax-plot-marker-none-gives-default-marker "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Prior to 1.5.3 keyword arguments passed to [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 were handled in two parts -- default keyword arguments generated internal to [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 (such as the cycled styles) and user supplied keyword arguments. The internally generated keyword arguments were passed to the [`matplotlib.lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 and the user keyword arguments were passed to `ln.set(**kwargs)` to update the artist after it was created. Now both sets of keyword arguments are merged and passed to [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
. This change was made to allow _None_ to be passed in via the user keyword arguments to mean 'do the default thing' as is the convention through out Matplotlib rather than raising an exception.

Unlike most [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 setter methods [`set_marker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker "matplotlib.lines.Line2D.set_marker")
 did accept [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 as a valid input which was mapped to 'no marker'. Thus, by routing this `marker=None` through `__init__` rather than `set(...)` the meaning of `ax.plot(..., marker=None)` changed from 'no markers' to 'default markers from rcparams'.

This is change is only evident if `mpl.rcParams['lines.marker']` has a value other than `'None'` (which is string `'None'` which means 'no marker').

On this page