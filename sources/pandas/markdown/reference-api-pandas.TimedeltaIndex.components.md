[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.components.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.TimedeltaIndex.components.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.components.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.TimedeltaIndex.components.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.TimedeltaIndex.components.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.TimedeltaIndex.components.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.TimedeltaIndex.components.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.TimedeltaIndex.components.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.TimedeltaIndex.components.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.TimedeltaIndex.components.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.TimedeltaIndex.components.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.TimedeltaIndex.components.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.TimedeltaIndex.components.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.TimedeltaIndex.components.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex.components[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.components.html#pandas-timedeltaindex-components "Link to this heading")

================================================================================================================================================================================

property TimedeltaIndex.components[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/timedeltas.py#L494-L522)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.components.html#pandas.TimedeltaIndex.components "Link to this definition")

Return a DataFrame of the individual resolution components of the Timedeltas.

The components (days, hours, minutes seconds, milliseconds, microseconds, nanoseconds) are returned as columns in a DataFrame.

Returns:

DataFrame

See also

`TimedeltaIndex.total_seconds`

Return total duration expressed in seconds.

[`Timedelta.components`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.components.html#pandas.Timedelta.components "pandas.Timedelta.components")

Return a components namedtuple-like of a single timedelta.

Examples

\>>> tdelta\_idx \= pd.to\_timedelta(\["1 day 3 min 2 us 42 ns"\])
\>>> tdelta\_idx
TimedeltaIndex(\['1 days 00:03:00.000002042'\],
               dtype='timedelta64\[ns\]', freq=None)
\>>> tdelta\_idx.components
   days  hours  minutes  seconds  milliseconds  microseconds  nanoseconds
0     1      0        3        0             0             2           42

Copy to clipboard

On this page