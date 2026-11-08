[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.seconds.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.seconds.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.seconds.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.seconds.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.seconds.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.seconds.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.seconds.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.seconds.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.seconds.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.seconds.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.seconds.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.seconds.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.seconds[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html#pandas-series-dt-seconds "Link to this heading")

========================================================================================================================================================

Series.dt.seconds[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html#pandas.Series.dt.seconds "Link to this definition")

Number of seconds (>= 0 and less than 1 day) for each element.

This attribute returns the seconds component of each timedelta value, which is the number of seconds remaining after subtracting whole days. Values range from 0 to 86399.

See also

[`Series.dt.seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html#pandas.Series.dt.seconds "pandas.Series.dt.seconds")

Return number of seconds for each element.

[`Series.dt.nanoseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanoseconds.html#pandas.Series.dt.nanoseconds "pandas.Series.dt.nanoseconds")

Return number of nanoseconds for each element.

Examples

For Series:

\>>> ser \= pd.Series(pd.to\_timedelta(\[1, 2, 3\], unit\='s'))
\>>> ser
0   0 days 00:00:01
1   0 days 00:00:02
2   0 days 00:00:03
dtype: timedelta64\[us\]
\>>> ser.dt.seconds
0    1
1    2
2    3
dtype: int32

Copy to clipboard

For TimedeltaIndex:

\>>> tdelta\_idx \= pd.to\_timedelta(\[1, 2, 3\], unit\='s')
\>>> tdelta\_idx
TimedeltaIndex(\['0 days 00:00:01', '0 days 00:00:02', '0 days 00:00:03'\],
               dtype='timedelta64\[us\]', freq=None)
\>>> tdelta\_idx.seconds
Index(\[1, 2, 3\], dtype='int32')

Copy to clipboard

On this page