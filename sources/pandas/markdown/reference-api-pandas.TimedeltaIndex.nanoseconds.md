[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.nanoseconds.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.TimedeltaIndex.nanoseconds.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.TimedeltaIndex.nanoseconds.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex.nanoseconds[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.nanoseconds.html#pandas-timedeltaindex-nanoseconds "Link to this heading")

===================================================================================================================================================================================

property TimedeltaIndex.nanoseconds[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/timedeltas.py#L468-L492)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.nanoseconds.html#pandas.TimedeltaIndex.nanoseconds "Link to this definition")

Number of nanoseconds (>= 0 and less than 1 microsecond) for each element.

This attribute returns the nanoseconds component of each timedelta value, which is the number of nanoseconds remaining after subtracting whole microseconds. Values range from 0 to 999.

See also

[`Series.dt.seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html#pandas.Series.dt.seconds "pandas.Series.dt.seconds")

Return number of seconds for each element.

[`Series.dt.microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microseconds.html#pandas.Series.dt.microseconds "pandas.Series.dt.microseconds")

Return number of microseconds for each element.

Examples

\>>> tdelta\_idx \= pd.to\_timedelta(\[1, 2, 3\], unit\="ns")
\>>> tdelta\_idx
TimedeltaIndex(\['0 days 00:00:00.000000001', '0 days 00:00:00.000000002',\
                '0 days 00:00:00.000000003'\],
               dtype='timedelta64\[ns\]', freq=None)
\>>> tdelta\_idx.nanoseconds
Index(\[1, 2, 3\], dtype='int32')

Copy to clipboard

On this page