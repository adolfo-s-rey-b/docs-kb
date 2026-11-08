[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.days.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.days.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.days.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.days.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.days.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.days.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.days.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.days.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.days.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.days.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.days.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.days.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.days[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days.html#pandas-series-dt-days "Link to this heading")

===============================================================================================================================================

Series.dt.days[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days.html#pandas.Series.dt.days "Link to this definition")

Number of days for each element.

This attribute returns the number of whole days in each timedelta value. It represents the days component of the duration, not the total duration expressed in days.

See also

[`Series.dt.seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html#pandas.Series.dt.seconds "pandas.Series.dt.seconds")

Return number of seconds for each element.

[`Series.dt.microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microseconds.html#pandas.Series.dt.microseconds "pandas.Series.dt.microseconds")

Return number of microseconds for each element.

[`Series.dt.nanoseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanoseconds.html#pandas.Series.dt.nanoseconds "pandas.Series.dt.nanoseconds")

Return number of nanoseconds for each element.

Examples

For Series:

\>>> ser \= pd.Series(pd.to\_timedelta(\[1, 2, 3\], unit\='D'))
\>>> ser
0   1 days
1   2 days
2   3 days
dtype: timedelta64\[us\]
\>>> ser.dt.days
0    1
1    2
2    3
dtype: int64

Copy to clipboard

For TimedeltaIndex:

\>>> tdelta\_idx \= pd.to\_timedelta(\["0 days", "10 days", "20 days"\])
\>>> tdelta\_idx
TimedeltaIndex(\['0 days', '10 days', '20 days'\],
                dtype='timedelta64\[us\]', freq=None)
\>>> tdelta\_idx.days
Index(\[0, 10, 20\], dtype='int64')

Copy to clipboard

On this page