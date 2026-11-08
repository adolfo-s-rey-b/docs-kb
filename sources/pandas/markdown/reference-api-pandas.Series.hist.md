[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.hist.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.hist.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.hist.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.hist.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.hist.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.hist.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.hist.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.hist.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.hist.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.hist.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.hist.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.hist.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.hist.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.hist.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.hist[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.hist.html#pandas-series-hist "Link to this heading")

======================================================================================================================================

Series.hist(_by\=None_, _ax\=None_, _grid\=True_, _xlabelsize\=None_, _xrot\=None_, _ylabelsize\=None_, _yrot\=None_, _figsize\=None_, _bins\=10_, _backend\=None_, _legend\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L49-L149)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.hist.html#pandas.Series.hist "Link to this definition")

Draw histogram of the input series using matplotlib.

The histogram is computed over the fixed or variable width bins, and drawn using the matplotlib library. This is useful for visualizing the distribution of the data.

Parameters:

**by**object, optional

If passed, then used to form histograms for separate groups.

**ax**matplotlib axis object

If not passed, uses gca().

**grid**bool, default True

Whether to show axis grid lines.

**xlabelsize**int, default None

If specified changes the x-axis label size.

**xrot**float, default None

Rotation of x axis labels.

**ylabelsize**int, default None

If specified changes the y-axis label size.

**yrot**float, default None

Rotation of y axis labels.

**figsize**tuple, default None

Figure size in inches by default.

**bins**int or sequence, default 10

Number of histogram bins to be used. If an integer is given, bins + 1 bin edges are calculated and returned. If bins is a sequence, gives bin edges, including left edge of first bin and right edge of last bin. In this case, bins is returned unmodified.

**backend**str, default None

Backend to use instead of the backend specified in the option `plotting.backend`. For instance, ‘matplotlib’. Alternatively, to specify the `plotting.backend` for the whole session, set `pd.options.plotting.backend`.

**legend**bool, default False

Whether to show the legend.

**\*\*kwargs**

To be passed to the actual plotting function.

Returns:

matplotlib.axes.Axes

A histogram plot.

See also

[`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "(in Matplotlib v3.11.2)")

Plot a histogram using matplotlib.

Examples

For Series:

\>>> lst \= \["a", "a", "a", "b", "b", "b"\]
\>>> ser \= pd.Series(\[1, 2, 2, 4, 6, 6\], index\=lst)
\>>> hist \= ser.hist()

Copy to clipboard

![../../_images/pandas-Series-hist-1.png](https://pandas.pydata.org/docs/_images/pandas-Series-hist-1.png)

For Groupby:

\>>> lst \= \["a", "a", "a", "b", "b", "b"\]
\>>> ser \= pd.Series(\[1, 2, 2, 4, 6, 6\], index\=lst)
\>>> hist \= ser.groupby(level\=0).hist()

Copy to clipboard

![../../_images/pandas-Series-hist-2.png](https://pandas.pydata.org/docs/_images/pandas-Series-hist-2.png)

On this page