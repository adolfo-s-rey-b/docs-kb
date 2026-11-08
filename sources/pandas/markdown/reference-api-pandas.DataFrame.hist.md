[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.hist.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.hist.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.hist.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.hist.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.hist.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.hist.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.hist.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.hist.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.hist.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.hist.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.hist.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.hist.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.hist[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html#pandas-dataframe-hist "Link to this heading")

===============================================================================================================================================

DataFrame.hist(_column\=None_, _by\=None_, _grid\=True_, _xlabelsize\=None_, _xrot\=None_, _ylabelsize\=None_, _yrot\=None_, _ax\=None_, _sharex\=False_, _sharey\=False_, _figsize\=None_, _layout\=None_, _bins\=10_, _backend\=None_, _legend\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L152-L279)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html#pandas.DataFrame.hist "Link to this definition")

Make a histogram of the DataFrame’s columns.

A [histogram](https://en.wikipedia.org/wiki/Histogram)
 is a representation of the distribution of data. This function calls `matplotlib.pyplot.hist()`, on each series in the DataFrame, resulting in one histogram per column.

Parameters:

**data**DataFrame

The pandas object holding the data.

**column**str or sequence, optional

If passed, will be used to limit data to a subset of columns.

**by**object, optional

If passed, then used to form histograms for separate groups.

**grid**bool, default True

Whether to show axis grid lines.

**xlabelsize**int, default None

If specified changes the x-axis label size.

**xrot**float, default None

Rotation of x axis labels. For example, a value of 90 displays the x labels rotated 90 degrees clockwise.

**ylabelsize**int, default None

If specified changes the y-axis label size.

**yrot**float, default None

Rotation of y axis labels. For example, a value of 90 displays the y labels rotated 90 degrees clockwise.

**ax**Matplotlib axes object, default None

The axes to plot the histogram on.

**sharex**bool, default True if ax is None else False

In case subplots=True, share x axis and set some x axis labels to invisible; defaults to True if ax is None otherwise False if an ax is passed in. Note that passing in both an ax and sharex=True will alter all x axis labels for all subplots in a figure.

**sharey**bool, default False

In case subplots=True, share y axis and set some y axis labels to invisible.

**figsize**tuple, optional

The size in inches of the figure to create. Uses the value in matplotlib.rcParams by default.

**layout**tuple, optional

Tuple of (rows, columns) for the layout of the histograms.

**bins**int or sequence, default 10

Number of histogram bins to be used. If an integer is given, bins + 1 bin edges are calculated and returned. If bins is a sequence, gives bin edges, including left edge of first bin and right edge of last bin. In this case, bins is returned unmodified.

**backend**str, default None

Backend to use instead of the backend specified in the option `plotting.backend`. For instance, ‘matplotlib’. Alternatively, to specify the `plotting.backend` for the whole session, set `pd.options.plotting.backend`.

**legend**bool, default False

Whether to show the legend.

**\*\*kwargs**

All other plotting keyword arguments to be passed to `matplotlib.pyplot.hist()`.

Returns:

np.ndarray

2D NumPy Array of [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.2)")
.

See also

[`matplotlib.pyplot.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "(in Matplotlib v3.11.2)")

Plot a histogram using matplotlib.

Examples

This example draws a histogram based on the length and width of some animals, displayed in three bins

\>>> data \= {
...     "length": \[1.5, 0.5, 1.2, 0.9, 3\],
...     "width": \[0.7, 0.2, 0.15, 0.2, 1.1\],
... }
\>>> index \= \["pig", "rabbit", "duck", "chicken", "horse"\]
\>>> df \= pd.DataFrame(data, index\=index)
\>>> hist \= df.hist(bins\=3)

Copy to clipboard

![../../_images/pandas-DataFrame-hist-1.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-hist-1.png)

On this page