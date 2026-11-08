[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanoseconds.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.nanoseconds[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanoseconds.html#pandas-series-dt-nanoseconds "Link to this heading")

====================================================================================================================================================================

Series.dt.nanoseconds[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanoseconds.html#pandas.Series.dt.nanoseconds "Link to this definition")

Number of nanoseconds (>= 0 and less than 1 microsecond) for each element.

This attribute returns the nanoseconds component of each timedelta value, which is the number of nanoseconds remaining after subtracting whole microseconds. Values range from 0 to 999.

See also

[`Series.dt.seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html#pandas.Series.dt.seconds "pandas.Series.dt.seconds")

Return number of seconds for each element.

[`Series.dt.microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microseconds.html#pandas.Series.dt.microseconds "pandas.Series.dt.microseconds")

Return number of microseconds for each element.

Examples

For Series:

\>>> ser \= pd.Series(pd.to\_timedelta(\[1, 2, 3\], unit\='ns'))
\>>> ser
0   0 days 00:00:00.000000001
1   0 days 00:00:00.000000002
2   0 days 00:00:00.000000003
dtype: timedelta64\[ns\]
\>>> ser.dt.nanoseconds
0    1
1    2
2    3
dtype: int32

Copy to clipboard

For TimedeltaIndex:

\>>> tdelta\_idx \= pd.to\_timedelta(\[1, 2, 3\], unit\='ns')
\>>> tdelta\_idx
TimedeltaIndex(\['0 days 00:00:00.000000001', '0 days 00:00:00.000000002',\
                '0 days 00:00:00.000000003'\],
               dtype='timedelta64\[ns\]', freq=None)
\>>> tdelta\_idx.nanoseconds
Index(\[1, 2, 3\], dtype='int32')

Copy to clipboard

On this page