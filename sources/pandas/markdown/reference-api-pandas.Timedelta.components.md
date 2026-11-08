[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.components.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.components[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.components.html#pandas-timedelta-components "Link to this heading")

=================================================================================================================================================================

Timedelta.components[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.components.html#pandas.Timedelta.components "Link to this definition")

Return a components namedtuple-like.

Each component represents a different time unit, allowing you to access the breakdown of the total duration in terms of days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds.

See also

[`Timedelta.total_seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html#pandas.Timedelta.total_seconds "pandas.Timedelta.total_seconds")

Returns the total duration of the Timedelta in seconds.

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to Timedelta.

[`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")

Represents a duration, the difference between two dates or times.

Examples

\>>> td \= pd.Timedelta('2 day 4 min 3 us 42 ns')
\>>> td.components
Components(days=2, hours=0, minutes=4, seconds=0, milliseconds=0,
    microseconds=3, nanoseconds=42)

Copy to clipboard

On this page