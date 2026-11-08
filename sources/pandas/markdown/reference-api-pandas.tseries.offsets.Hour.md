[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Hour.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.Hour[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Hour.html#pandas-tseries-offsets-hour "Link to this heading")

=================================================================================================================================================================

class pandas.tseries.offsets.Hour[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Hour.html#pandas.tseries.offsets.Hour "Link to this definition")

Offset `n` hours.

Represents a fixed duration of `n` hours (3,600 seconds each) for use in arithmetic with datetime-like objects. Unlike calendar-based offsets, the result is deterministic and does not depend on timezone or daylight saving.

Parameters:

**n**int, default 1

The number of hours represented.

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

You can use the parameter `n` to represent a shift of n hours.

\>>> from pandas.tseries.offsets import Hour
\>>> ts \= pd.Timestamp(2022, 12, 9, 15)
\>>> ts
Timestamp('2022-12-09 15:00:00')

Copy to clipboard

\>>> ts + Hour()
Timestamp('2022-12-09 16:00:00')
\>>> ts \- Hour(4)
Timestamp('2022-12-09 11:00:00')

Copy to clipboard

\>>> ts + Hour(\-4)
Timestamp('2022-12-09 11:00:00')

Copy to clipboard

On this page