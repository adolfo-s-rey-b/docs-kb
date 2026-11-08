[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microseconds.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.microseconds.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microseconds.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.microseconds.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.microseconds.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.microseconds.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.microseconds.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.microseconds.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.microseconds.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.microseconds.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.microseconds.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.microseconds.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.microseconds.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.microseconds.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.microseconds[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microseconds.html#pandas-series-dt-microseconds "Link to this heading")

=======================================================================================================================================================================

Series.dt.microseconds[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microseconds.html#pandas.Series.dt.microseconds "Link to this definition")

Number of microseconds (>= 0 and less than 1 second) for each element.

This attribute returns the microseconds component of each timedelta value, which is the number of microseconds remaining after subtracting whole seconds. Values range from 0 to 999999.

See also

`pd.Timedelta.microseconds`

Number of microseconds (>= 0 and less than 1 second).

`pd.Timedelta.to_pytimedelta.microseconds`

Number of microseconds (>= 0 and less than 1 second) of a datetime.timedelta.

Examples

For Series:

\>>> ser \= pd.Series(pd.to\_timedelta(\[1, 2, 3\], unit\='us'))
\>>> ser
0   0 days 00:00:00.000001
1   0 days 00:00:00.000002
2   0 days 00:00:00.000003
dtype: timedelta64\[us\]
\>>> ser.dt.microseconds
0    1
1    2
2    3
dtype: int32

Copy to clipboard

For TimedeltaIndex:

\>>> tdelta\_idx \= pd.to\_timedelta(\[1, 2, 3\], unit\='us')
\>>> tdelta\_idx
TimedeltaIndex(\['0 days 00:00:00.000001', '0 days 00:00:00.000002',\
                '0 days 00:00:00.000003'\],
               dtype='timedelta64\[us\]', freq=None)
\>>> tdelta\_idx.microseconds
Index(\[1, 2, 3\], dtype='int32')

Copy to clipboard

On this page