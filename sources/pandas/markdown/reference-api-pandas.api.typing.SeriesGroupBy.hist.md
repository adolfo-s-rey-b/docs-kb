[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.hist.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.hist.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.hist[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.hist.html#pandas-api-typing-seriesgroupby-hist "Link to this heading")

============================================================================================================================================================================================

SeriesGroupBy.hist(_by\=None_, _ax\=None_, _grid\=True_, _xlabelsize\=None_, _xrot\=None_, _ylabelsize\=None_, _yrot\=None_, _figsize\=None_, _bins\=10_, _backend\=None_, _legend\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1931-L2010)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.hist.html#pandas.api.typing.SeriesGroupBy.hist "Link to this definition")

Draw histogram for each group’s values using `Series.hist()` API.

A separate histogram subplot is generated for each group, making it easy to visually compare the distribution of values across groups.

Parameters:

**by**object, optional

Grouping key.

**ax**matplotlib.axes.Axes, optional

Axis to draw the histogram on.

**grid**bool, default True

Show axis grid lines.

**xlabelsize**int, default None

X axis label size.

**xrot**float, default None

Rotation for x ticks.

**ylabelsize**int, default None

Y axis label size.

**yrot**float, default None

Rotation for y ticks.

**figsize**tuple, optional

Figure size in inches.

**bins**int or sequence, default 10

Number of histogram bins or bin edges.

**backend**str or callable or None, optional

Plotting backend to use (e.g. ‘matplotlib’). If None, use the default plotting backend.

**legend**bool, default False

Whether to draw the legend.

**\*\*kwargs**

Additional keyword arguments passed to `Series.hist()`.

Returns:

matplotlib.axes.Axes or ndarray of Axes

The returned matplotlib axes or array of axes depending on input.

See also

`Series.hist`

Equivalent histogram plotting method on Series.

Examples

\>>> df \= pd.DataFrame({"val": \[1, 2, 2, 3, 3, 3\]}, index\=\[0, 0, 1, 1, 2, 2\])
\>>> g \= df\["val"\].groupby(\[0, 0, 1, 1, 2, 2\])
\>>> g.hist()

Copy to clipboard

On this page