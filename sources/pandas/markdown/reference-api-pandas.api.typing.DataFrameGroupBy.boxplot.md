[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.boxplot[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html#pandas-api-typing-dataframegroupby-boxplot "Link to this heading")

==============================================================================================================================================================================================================

DataFrameGroupBy.boxplot(_subplots\=True_, _column\=None_, _fontsize\=None_, _rot\=0_, _grid\=True_, _ax\=None_, _figsize\=None_, _layout\=None_, _sharex\=False_, _sharey\=True_, _backend\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L676-L781)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html#pandas.api.typing.DataFrameGroupBy.boxplot "Link to this definition")

Make box plots from DataFrameGroupBy data.

Creates one or more box-and-whisker plots based on data that has been grouped using `DataFrame.groupby()`. Each group can be rendered as a separate subplot or combined into a single figure.

Parameters:

**grouped**DataFrameGroupBy

The grouped DataFrame object over which to create the box plots.

**subplots**bool

*   `False` - no subplots will be used
    
*   `True` - create a subplot for each group.
    

**column**column name or list of names, or vector

Can be any valid input to groupby.

**fontsize**float or str

Font size for the labels.

**rot**float

Rotation angle of labels (in degrees) on the x-axis.

**grid**bool

Whether to show grid lines on the plot.

**ax**Matplotlib axis object, default None

The axes on which to draw the plots. If None, uses the current axes.

**figsize**tuple of (float, float)

The figure size in inches (width, height).

**layout**tuple (optional)

The layout of the plot: (rows, columns).

**sharex**bool, default False

Whether x-axes will be shared among subplots.

**sharey**bool, default True

Whether y-axes will be shared among subplots.

**backend**str, default None

Backend to use instead of the backend specified in the option `plotting.backend`. For instance, ‘matplotlib’. Alternatively, to specify the `plotting.backend` for the whole session, set `pd.options.plotting.backend`.

**\*\*kwargs**

All other plotting keyword arguments to be passed to matplotlib’s boxplot function.

Returns:

dict or DataFrame.boxplot return value

If `subplots=True`, returns a dictionary of group keys to the boxplot return values. If `subplots=False`, returns the boxplot return value of a single DataFrame.

See also

`DataFrame.boxplot`

Create a box plot from a DataFrame.

`Series.plot`

Plot a Series.

Examples

You can create boxplots for grouped data and show them as separate subplots:

\>>> import itertools
\>>> tuples \= \[t for t in itertools.product(range(1000), range(4))\]
\>>> index \= pd.MultiIndex.from\_tuples(tuples, names\=\["lvl0", "lvl1"\])
\>>> data \= np.random.default\_rng(42).standard\_normal((len(index), 4))
\>>> df \= pd.DataFrame(data, columns\=list("ABCD"), index\=index)
\>>> grouped \= df.groupby(level\="lvl1")
\>>> grouped.boxplot(rot\=45, fontsize\=12, figsize\=(8, 10))

Copy to clipboard

![../../_images/pandas-api-typing-DataFrameGroupBy-boxplot-1.png](https://pandas.pydata.org/docs/_images/pandas-api-typing-DataFrameGroupBy-boxplot-1.png)

The `subplots=False` option shows the boxplots in a single figure.

\>>> grouped.boxplot(subplots\=False, rot\=45, fontsize\=12)

Copy to clipboard

![../../_images/pandas-api-typing-DataFrameGroupBy-boxplot-2.png](https://pandas.pydata.org/docs/_images/pandas-api-typing-DataFrameGroupBy-boxplot-2.png)

On this page