[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex.to\_pytimedelta[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html#pandas-timedeltaindex-to-pytimedelta "Link to this heading")

=============================================================================================================================================================================================

TimedeltaIndex.to\_pytimedelta()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/timedeltas.py#L524-L554)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html#pandas.TimedeltaIndex.to_pytimedelta "Link to this definition")

Return an ndarray of datetime.timedelta objects.

Each element of the [`TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")
 is converted to the corresponding native Python [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
 object.

Returns:

numpy.ndarray

Object-dtype array of [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
.

See also

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to timedelta format.

[`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")

Represents a duration between two dates or times.

[`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")

Index of datetime64 data.

[`Timedelta.components`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.components.html#pandas.Timedelta.components "pandas.Timedelta.components")

Return a components namedtuple-like of a single timedelta.

Examples

\>>> tdelta\_idx \= pd.to\_timedelta(\[1, 2, 3\], unit\="D")
\>>> tdelta\_idx
TimedeltaIndex(\['1 days', '2 days', '3 days'\],
                dtype='timedelta64\[us\]', freq=None)
\>>> tdelta\_idx.to\_pytimedelta()
array(\[datetime.timedelta(days=1), datetime.timedelta(days=2),\
       datetime.timedelta(days=3)\], dtype=object)

Copy to clipboard

On this page