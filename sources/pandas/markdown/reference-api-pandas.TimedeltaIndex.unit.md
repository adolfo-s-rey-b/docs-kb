[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.unit.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex.unit[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.unit.html#pandas-timedeltaindex-unit "Link to this heading")

==============================================================================================================================================================

property TimedeltaIndex.unit[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimelike.py#L917-L957)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.unit.html#pandas.TimedeltaIndex.unit "Link to this definition")

The precision unit of the datetime data.

Returns the precision unit for the dtype of the index. This is the smallest time frame that can be stored within this dtype.

Returns:

str

Unit string representation (e.g. `"ns"`).

See also

[`DatetimeIndex.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.as_unit.html#pandas.DatetimeIndex.as_unit "pandas.DatetimeIndex.as_unit")

Convert to the given unit.

[`TimedeltaIndex.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.as_unit.html#pandas.TimedeltaIndex.as_unit "pandas.TimedeltaIndex.as_unit")

Convert to the given unit.

Examples

For a DatetimeIndex:

\>>> idx \= pd.DatetimeIndex(\["2020-01-02 01:02:03.004005006"\])
\>>> idx.unit
'ns'

Copy to clipboard

\>>> idx\_s \= pd.DatetimeIndex(\["2020-01-02 01:02:03"\], dtype\="datetime64\[s\]")
\>>> idx\_s.unit
's'

Copy to clipboard

For a TimedeltaIndex:

\>>> tdidx \= pd.TimedeltaIndex(\["1 day 3 min 2 us 42 ns"\])
\>>> tdidx.unit
'ns'

Copy to clipboard

\>>> tdidx\_s \= pd.TimedeltaIndex(\["1 day 3 min"\], dtype\="timedelta64\[s\]")
\>>> tdidx\_s.unit
's'

Copy to clipboard

On this page