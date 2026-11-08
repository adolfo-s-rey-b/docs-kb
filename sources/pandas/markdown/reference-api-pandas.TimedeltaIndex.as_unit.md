[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.as_unit.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex.as\_unit[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.as_unit.html#pandas-timedeltaindex-as-unit "Link to this heading")

========================================================================================================================================================================

TimedeltaIndex.as\_unit(_unit_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimelike.py#L959-L1006)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.as_unit.html#pandas.TimedeltaIndex.as_unit "Link to this definition")

Convert to a dtype with the given unit resolution.

This method is for converting the dtype of a `DatetimeIndex` or `TimedeltaIndex` to a new dtype with the given unit resolution/precision.

Parameters:

**unit**{‘s’, ‘ms’, ‘us’, ‘ns’}

Returns:

same type as self

Converted to the specified unit.

See also

[`Timestamp.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.as_unit.html#pandas.Timestamp.as_unit "pandas.Timestamp.as_unit")

Convert to the given unit.

[`Timedelta.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.as_unit.html#pandas.Timedelta.as_unit "pandas.Timedelta.as_unit")

Convert to the given unit.

[`DatetimeIndex.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.as_unit.html#pandas.DatetimeIndex.as_unit "pandas.DatetimeIndex.as_unit")

Convert to the given unit.

[`TimedeltaIndex.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.as_unit.html#pandas.TimedeltaIndex.as_unit "pandas.TimedeltaIndex.as_unit")

Convert to the given unit.

Examples

For [`pandas.DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
:

\>>> idx \= pd.DatetimeIndex(\["2020-01-02 01:02:03.004005006"\])
\>>> idx
DatetimeIndex(\['2020-01-02 01:02:03.004005006'\],
              dtype='datetime64\[ns\]', freq=None)
\>>> idx.as\_unit("s")
DatetimeIndex(\['2020-01-02 01:02:03'\], dtype='datetime64\[s\]', freq=None)

Copy to clipboard

For [`pandas.TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")
:

\>>> tdelta\_idx \= pd.to\_timedelta(\["1 day 3 min 2 us 42 ns"\])
\>>> tdelta\_idx
TimedeltaIndex(\['1 days 00:03:00.000002042'\],
                dtype='timedelta64\[ns\]', freq=None)
\>>> tdelta\_idx.as\_unit("s")
TimedeltaIndex(\['1 days 00:03:00'\], dtype='timedelta64\[s\]', freq=None)

Copy to clipboard

On this page