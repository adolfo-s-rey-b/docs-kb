[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pydatetime.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.to_pydatetime.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pydatetime.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.to_pydatetime.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.to_pydatetime.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.to_pydatetime.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.to_pydatetime.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.to_pydatetime.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.to_pydatetime.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.to_pydatetime.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.to_pydatetime.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.to_pydatetime.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.to_pydatetime.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.to_pydatetime.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.to\_pydatetime[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pydatetime.html#pandas-series-dt-to-pydatetime "Link to this heading")

===========================================================================================================================================================================

Series.dt.to\_pydatetime()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/accessors.py#L327-L381)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pydatetime.html#pandas.Series.dt.to_pydatetime "Link to this definition")

Return the data as a Series of [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
 objects.

Timezone information is retained if present.

Warning

Python’s datetime uses microsecond resolution, which is lower than pandas (nanosecond). The values are truncated.

Returns:

Series

Series containing native Python datetime objects.

See also

[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")

Standard library value for a datetime.

Examples

\>>> s \= pd.Series(pd.date\_range("20180310", periods\=2))
\>>> s
0   2018-03-10
1   2018-03-11
dtype: datetime64\[us\]

Copy to clipboard

\>>> s.dt.to\_pydatetime()
0    2018-03-10 00:00:00
1    2018-03-11 00:00:00
dtype: object

Copy to clipboard

pandas’ nanosecond precision is truncated to microseconds.

\>>> s \= pd.Series(pd.date\_range("20180310", periods\=2, freq\="ns"))
\>>> s
0   2018-03-10 00:00:00.000000000
1   2018-03-10 00:00:00.000000001
dtype: datetime64\[ns\]

Copy to clipboard

\>>> s.dt.to\_pydatetime()
0    2018-03-10 00:00:00
1    2018-03-10 00:00:00
dtype: object

Copy to clipboard

On this page