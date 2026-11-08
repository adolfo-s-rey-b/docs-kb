[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.quantile[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html#pandas-api-typing-seriesgroupby-quantile "Link to this heading")

========================================================================================================================================================================================================

SeriesGroupBy.quantile(_q\=0.5_, _interpolation\='linear'_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L4400-L4548)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html#pandas.api.typing.SeriesGroupBy.quantile "Link to this definition")

Return group values at the given quantile, a la numpy.percentile.

This method returns the value at the given quantile for each group, using the specified interpolation method when the desired quantile falls between two data points.

Parameters:

**q**float or array-like, default 0.5 (50% quantile)

Value(s) between 0 and 1 providing the quantile(s) to compute.

**interpolation**{‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}

Method to use when the desired quantile falls between two points.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 2.0.0: numeric\_only now defaults to `False`.

Returns:

Series or DataFrame

Return type determined by caller of GroupBy object.

See also

`Series.quantile`

Similar method for Series.

`DataFrame.quantile`

Similar method for DataFrame.

[`numpy.percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "(in NumPy v2.5)")

NumPy method to compute qth percentile.

Examples

\>>> df \= pd.DataFrame(
...     \[\["a", 1\], \["a", 2\], \["a", 3\], \["b", 1\], \["b", 3\], \["b", 5\]\],
...     columns\=\["key", "val"\],
... )
\>>> df.groupby("key").quantile()
    val
key
a    2.0
b    3.0

Copy to clipboard

On this page