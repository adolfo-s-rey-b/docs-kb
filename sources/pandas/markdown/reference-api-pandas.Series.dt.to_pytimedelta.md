[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pytimedelta.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.to\_pytimedelta[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pytimedelta.html#pandas-series-dt-to-pytimedelta "Link to this heading")

==============================================================================================================================================================================

Series.dt.to\_pytimedelta()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/accessors.py#L548-L592)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pytimedelta.html#pandas.Series.dt.to_pytimedelta "Link to this definition")

Return an array of native [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
 objects.

Python’s standard datetime library uses a different representation timedelta’s. This method converts a Series of pandas Timedeltas to datetime.timedelta format with the same length as the original Series.

Returns:

numpy.ndarray

Array of 1D containing data with datetime.timedelta type.

See also

[`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")

A duration expressing the difference between two date, time, or datetime.

Examples

\>>> s \= pd.Series(pd.to\_timedelta(np.arange(5), unit\="D"))
\>>> s
0   0 days
1   1 days
2   2 days
3   3 days
4   4 days
dtype: timedelta64\[us\]

Copy to clipboard

\>>> s.dt.to\_pytimedelta()
array(\[datetime.timedelta(0), datetime.timedelta(days=1),\
datetime.timedelta(days=2), datetime.timedelta(days=3),\
datetime.timedelta(days=4)\], dtype=object)

Copy to clipboard

On this page