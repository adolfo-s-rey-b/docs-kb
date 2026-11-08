[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplot_mosaic.html#main-content)

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
    

matplotlib.figure.SubFigure.subplot\_mosaic[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplot_mosaic.html#matplotlib-figure-subfigure-subplot-mosaic "Link to this heading")

============================================================================================================================================================================================================

SubFigure.subplot\_mosaic(_mosaic_, _\*_, _sharex\=False_, _sharey\=False_, _width\_ratios\=None_, _height\_ratios\=None_, _empty\_sentinel\='.'_, _subplot\_kw\=None_, _per\_subplot\_kw\=None_, _gridspec\_kw\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1906-L2213)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplot_mosaic.html#matplotlib.figure.SubFigure.subplot_mosaic "Link to this definition")

Build a layout of Axes based on ASCII art or nested lists.

This is a helper function to build complex GridSpec layouts visually.

See [Complex and semantic figure composition (subplot\_mosaic)](https://matplotlib.org/stable/users/explain/axes/mosaic.html#mosaic)
 for an example and full API documentation

Parameters:

**mosaic**list of list of {hashable or nested} or str

A visual layout of how you want your Axes to be arranged labeled as strings. For example

x \= \[\['A panel', 'A panel', 'edge'\],\
     \['C panel', '.',       'edge'\]\]

produces 4 Axes:

*   'A panel' which is 1 row high and spans the first two columns
    
*   'edge' which is 2 rows high and is on the right edge
    
*   'C panel' which in 1 row and 1 column wide in the bottom left
    
*   a blank space 1 row and 1 column wide in the bottom center
    

Any of the entries in the layout can be a list of lists of the same form to create nested layouts.

If input is a str, then it can either be a multi-line string of the form

'''
AAE
C.E
'''

where each character is a column and each line is a row. Or it can be a single-line string where rows are separated by `;`:

'AB;CC'

The string notation allows only single character Axes labels and does not support nesting but is very terse.

The Axes identifiers may be [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 or a non-iterable hashable object (e.g. [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")
 s may not be used).

**sharex, sharey**bool, default: False

If True, the x-axis (_sharex_) or y-axis (_sharey_) will be shared among all subplots. In that case, tick label visibility and axis units behave as for [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplots.html#matplotlib.figure.SubFigure.subplots "matplotlib.figure.SubFigure.subplots")
. If False, each subplot's x- or y-axis will be independent.

**width\_ratios**array-like of length _ncols_, optional

Defines the relative widths of the columns. Each column gets a relative width of `width_ratios[i] / sum(width_ratios)`. If not given, all columns will have the same width. Equivalent to `gridspec_kw={'width_ratios': [...]}`. In the case of nested layouts, this argument applies only to the outer layout.

**height\_ratios**array-like of length _nrows_, optional

Defines the relative heights of the rows. Each row gets a relative height of `height_ratios[i] / sum(height_ratios)`. If not given, all rows will have the same height. Equivalent to `gridspec_kw={'height_ratios': [...]}`. In the case of nested layouts, this argument applies only to the outer layout.

**subplot\_kw**dict, optional

Dictionary with keywords passed to the [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 call used to create each subplot. These values may be overridden by values in _per\_subplot\_kw_.

**per\_subplot\_kw**dict, optional

A dictionary mapping the Axes identifiers or tuples of identifiers to a dictionary of keyword arguments to be passed to the [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 call used to create each subplot. The values in these dictionaries have precedence over the values in _subplot\_kw_.

If _mosaic_ is a string, and thus all keys are single characters, it is possible to use a single string instead of a tuple as keys; i.e. `"AB"` is equivalent to `("A", "B")`.

Added in version 3.7.

**gridspec\_kw**dict, optional

Dictionary with keywords passed to the [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 constructor used to create the grid the subplots are placed on. In the case of nested layouts, this argument applies only to the outer layout. For more complex layouts, users should use [`Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 to create the nesting.

**empty\_sentinel**object, optional

Entry in the layout to mean "leave this space empty". Defaults to `'.'`. Note, if _layout_ is a string, it is processed via [`inspect.cleandoc`](https://docs.python.org/3/library/inspect.html#inspect.cleandoc "(in Python v3.14)")
 to remove leading white space, which may interfere with using white-space as the empty sentinel.

Returns:

dict\[label, Axes\]

A dictionary mapping the labels to the Axes objects. The order of the Axes is left-to-right and top-to-bottom of their position in the total layout.

Examples using `matplotlib.figure.SubFigure.subplot_mosaic`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplot_mosaic.html#examples-using-matplotlib-figure-subfigure-subplot-mosaic "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_mosaic_thumb.png)

[Complex and semantic figure composition (subplot\_mosaic)](https://matplotlib.org/stable/users/explain/axes/mosaic.html)

Complex and semantic figure composition (subplot\_mosaic)

On this page