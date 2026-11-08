[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.boxplot.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.plotting.boxplot.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.plotting.boxplot.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.plotting.boxplot.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.plotting.boxplot.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.plotting.boxplot.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.plotting.boxplot.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.plotting.boxplot.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.plotting.boxplot.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.plotting.boxplot.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.plotting.boxplot.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.plotting.boxplot.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.plotting.boxplot.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.plotting.boxplot.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.boxplot[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.boxplot.html#pandas-plotting-boxplot "Link to this heading")

=====================================================================================================================================================

pandas.plotting.boxplot(_data_, _column\=None_, _by\=None_, _ax\=None_, _fontsize\=None_, _rot\=0_, _grid\=True_, _figsize\=None_, _layout\=None_, _return\_type\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L282-L469)
[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.boxplot.html#pandas.plotting.boxplot "Link to this definition")

Make a box plot from DataFrame columns.

Make a box-and-whisker plot from DataFrame columns, optionally grouped by some other columns. A box plot is a method for graphically depicting groups of numerical data through their quartiles. The box extends from the Q1 to Q3 quartile values of the data, with a line at the median (Q2). The whiskers extend from the edges of box to show the range of the data. By default, they extend no more than 1.5 \* IQR (IQR = Q3 - Q1) from the edges of the box, ending at the farthest data point within that interval. Outliers are plotted as separate dots.

For further details see Wikipedia’s entry for [boxplot](https://en.wikipedia.org/wiki/Box_plot)
.

Parameters:

**data**DataFrame

The data to visualize.

**column**str or list of str, optional

Column name or list of names, or vector. Can be any valid input to [`pandas.DataFrame.groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")
.

**by**str or array-like, optional

Column in the DataFrame to [`pandas.DataFrame.groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")
. One box-plot will be done per value of columns in by.

**ax**object of class matplotlib.axes.Axes, optional

The matplotlib axes to be used by boxplot.

**fontsize**float or str

Tick label font size in points or as a string (e.g., large).

**rot**float, default 0

The rotation angle of labels (in degrees) with respect to the screen coordinate system.

**grid**bool, default True

Setting this to True will show the grid.

**figsize**A tuple (width, height) in inches

The size of the figure to create in matplotlib.

**layout**tuple (rows, columns), optional

For example, (3, 5) will display the subplots using 3 rows and 5 columns, starting from the top-left.

**return\_type**{‘axes’, ‘dict’, ‘both’} or None, default ‘axes’

The kind of object to return. The default is `axes`.

*   ‘axes’ returns the matplotlib axes the boxplot is drawn on.
    
*   ‘dict’ returns a dictionary whose values are the matplotlib lines of the boxplot.
    
*   ‘both’ returns a namedtuple with the axes and dict.
    
*   when grouping with `by`, a Series mapping columns to `return_type` is returned.
    

If `return_type` is None, a NumPy array of axes with the same shape as `layout` is returned.

**\*\*kwargs**

All other plotting keyword arguments to be passed to [`matplotlib.pyplot.boxplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "(in Matplotlib v3.11.2)")
.

Returns:

result

See Notes.

See also

`Series.plot.hist`

Make a histogram.

[`matplotlib.pyplot.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "(in Matplotlib v3.11.2)")

Matplotlib equivalent plot.

Notes

The return type depends on the return\_type parameter:

*   ‘axes’ : object of class matplotlib.axes.Axes
    
*   ‘dict’ : dict of matplotlib.lines.Line2D objects
    
*   ‘both’ : a namedtuple with structure (ax, lines)
    

For data grouped with `by`, return a Series of the above or a numpy array:

*   [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
    
*   `array` (for `return_type = None`)
    

Use `return_type='dict'` when you want to tweak the appearance of the lines after plotting. In this case a dict containing the Lines making up the boxes, caps, fliers, medians, and whiskers is returned.

Examples

Boxplots can be created for every column in the dataframe by `df.boxplot()` or indicating the columns to be used:

\>>> rng \= np.random.default\_rng(42)
\>>> df \= pd.DataFrame(
...     rng.standard\_normal((10, 4)), columns\=\["Col1", "Col2", "Col3", "Col4"\]
... )
\>>> boxplot \= df.boxplot(column\=\["Col1", "Col2", "Col3"\])

Copy to clipboard

![../../_images/pandas-plotting-boxplot-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-boxplot-1.png)

Boxplots of variables distributions grouped by the values of a third variable can be created using the option `by`. For instance:

\>>> df \= pd.DataFrame(rng.standard\_normal((10, 2)), columns\=\["Col1", "Col2"\])
\>>> df\["X"\] \= pd.Series(\["A", "A", "A", "A", "A", "B", "B", "B", "B", "B"\])
\>>> boxplot \= df.boxplot(by\="X")

Copy to clipboard

![../../_images/pandas-plotting-boxplot-2.png](https://pandas.pydata.org/docs/_images/pandas-plotting-boxplot-2.png)

A list of strings (i.e. `['X', 'Y']`) can be passed to boxplot in order to group the data by combination of the variables in the x-axis:

\>>> df \= pd.DataFrame(
...     rng.standard\_normal((10, 3)), columns\=\["Col1", "Col2", "Col3"\]
... )
\>>> df\["X"\] \= pd.Series(\["A", "A", "A", "A", "A", "B", "B", "B", "B", "B"\])
\>>> df\["Y"\] \= pd.Series(\["A", "B", "A", "B", "A", "B", "A", "B", "A", "B"\])
\>>> boxplot \= df.boxplot(column\=\["Col1", "Col2"\], by\=\["X", "Y"\])

Copy to clipboard

![../../_images/pandas-plotting-boxplot-3.png](https://pandas.pydata.org/docs/_images/pandas-plotting-boxplot-3.png)

The layout of boxplot can be adjusted giving a tuple to `layout`:

\>>> boxplot \= df.boxplot(column\=\["Col1", "Col2"\], by\="X", layout\=(2, 1))

Copy to clipboard

![../../_images/pandas-plotting-boxplot-4.png](https://pandas.pydata.org/docs/_images/pandas-plotting-boxplot-4.png)

Additional formatting can be done to the boxplot, like suppressing the grid (`grid=False`), rotating the labels in the x-axis (i.e. `rot=45`) or changing the fontsize (i.e. `fontsize=15`):

\>>> boxplot \= df.boxplot(grid\=False, rot\=45, fontsize\=15)

Copy to clipboard

![../../_images/pandas-plotting-boxplot-5.png](https://pandas.pydata.org/docs/_images/pandas-plotting-boxplot-5.png)

The parameter `return_type` can be used to select the type of element returned by boxplot. When `return_type='axes'` is selected, the matplotlib axes on which the boxplot is drawn are returned:

\>>> boxplot \= df.boxplot(column\=\["Col1", "Col2"\], return\_type\="axes")
\>>> type(boxplot)
<class 'matplotlib.axes.\_axes.Axes'>

Copy to clipboard

When grouping with `by`, a Series mapping columns to `return_type` is returned:

\>>> boxplot \= df.boxplot(column\=\["Col1", "Col2"\], by\="X", return\_type\="axes")
\>>> type(boxplot)
<class 'pandas.Series'>

Copy to clipboard

If `return_type` is None, a NumPy array of axes with the same shape as `layout` is returned:

\>>> boxplot \= df.boxplot(column\=\["Col1", "Col2"\], by\="X", return\_type\=None)
\>>> type(boxplot)
<class 'numpy.ndarray'>

Copy to clipboard

On this page