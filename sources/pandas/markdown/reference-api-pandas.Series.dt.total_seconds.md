[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.total_seconds.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.total_seconds.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.total_seconds.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.total_seconds.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.total_seconds.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.total_seconds.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.total_seconds.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.total_seconds.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.total_seconds.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.total_seconds.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.total_seconds.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.total_seconds.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.total_seconds.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.total_seconds.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.total\_seconds[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.total_seconds.html#pandas-series-dt-total-seconds "Link to this heading")

===========================================================================================================================================================================

Series.dt.total\_seconds()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/timedeltas.py#L856-L940)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.total_seconds.html#pandas.Series.dt.total_seconds "Link to this definition")

Return total duration of each element expressed in seconds.

This method is available directly on TimedeltaArray, TimedeltaIndex and on Series containing timedelta values under the `.dt` namespace.

Returns:

ndarray, Index or Series

When the calling object is a TimedeltaArray, the return type is ndarray. When the calling object is a TimedeltaIndex, the return type is an Index with a float64 dtype. When the calling object is a Series, the return type is Series of type float64 whose index is the same as the original.

See also

[`datetime.timedelta.total_seconds`](https://docs.python.org/3/library/datetime.html#datetime.timedelta.total_seconds "(in Python v3.15)")

Standard library version of this method.

[`TimedeltaIndex.components`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.components.html#pandas.TimedeltaIndex.components "pandas.TimedeltaIndex.components")

Return a DataFrame with components of each Timedelta.

Examples

**Series**

\>>> s \= pd.Series(pd.to\_timedelta(np.arange(5), unit\="D"))
\>>> s
0   0 days
1   1 days
2   2 days
3   3 days
4   4 days
dtype: timedelta64\[us\]

Copy to clipboard

\>>> s.dt.total\_seconds()
0         0.0
1     86400.0
2    172800.0
3    259200.0
4    345600.0
dtype: float64

Copy to clipboard

**TimedeltaIndex**

\>>> idx \= pd.to\_timedelta(np.arange(5), unit\="D")
\>>> idx
TimedeltaIndex(\['0 days', '1 days', '2 days', '3 days', '4 days'\],
               dtype='timedelta64\[us\]', freq=None)

Copy to clipboard

\>>> idx.total\_seconds()
Index(\[0.0, 86400.0, 172800.0, 259200.0, 345600.0\], dtype='float64')

Copy to clipboard

On this page