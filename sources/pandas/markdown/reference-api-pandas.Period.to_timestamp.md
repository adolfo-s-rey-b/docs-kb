[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.to_timestamp.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.to\_timestamp[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.to_timestamp.html#pandas-period-to-timestamp "Link to this heading")

===============================================================================================================================================================

Period.to\_timestamp(_freq\=None_, _how\='start'_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.to_timestamp.html#pandas.Period.to_timestamp "Link to this definition")

Return the Timestamp representation of the Period.

Uses the target frequency specified at the part of the period specified by how, which is either the start or the end.

If possible, gives microsecond-unit Timestamp. Otherwise gives nanosecond unit.

Parameters:

**freq**str or DateOffset

Target frequency. Default is ‘D’ if self.\_freq is week or longer and ‘S’ otherwise.

**how**{‘start’, ‘end’, ‘s’, ‘e’}, default ‘start’

Whether to use the start or end of the period. Case-insensitive.

Returns:

Timestamp

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

A class representing a single point in time.

[`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")

Represents a span of time with a fixed frequency.

[`PeriodIndex.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas.PeriodIndex.to_timestamp "pandas.PeriodIndex.to_timestamp")

Convert a PeriodIndex to a DatetimeIndex.

Examples

\>>> period \= pd.Period('2023-1-1', freq\='D')
\>>> timestamp \= period.to\_timestamp()
\>>> timestamp
Timestamp('2023-01-01 00:00:00')

Copy to clipboard

On this page