[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.days.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex.days[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.days.html#pandas-timedeltaindex-days "Link to this heading")

==============================================================================================================================================================

property TimedeltaIndex.days[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/timedeltas.py#L391-L415)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.days.html#pandas.TimedeltaIndex.days "Link to this definition")

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

\>>> tdelta\_idx \= pd.to\_timedelta(\["0 days", "10 days", "20 days"\])
\>>> tdelta\_idx
TimedeltaIndex(\['0 days', '10 days', '20 days'\],
                dtype='timedelta64\[us\]', freq=None)
\>>> tdelta\_idx.days
Index(\[0, 10, 20\], dtype='int64')

Copy to clipboard

On this page