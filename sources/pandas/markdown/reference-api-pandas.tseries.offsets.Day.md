[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Day.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.Day.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Day.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.Day.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.Day.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.Day.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.Day.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.Day.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.Day.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.Day.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.Day.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.Day.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.Day.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.Day.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.Day[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Day.html#pandas-tseries-offsets-day "Link to this heading")

==============================================================================================================================================================

class pandas.tseries.offsets.Day[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Day.html#pandas.tseries.offsets.Day "Link to this definition")

Offset `n` days.

Represents a calendar-day offset for use in arithmetic with [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
, [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
, or other datetime-like objects. Addition and subtraction shift the value by exactly `n` calendar days, with time-of-day preserved.

Parameters:

**n**int, default 1

The number of days represented.

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

You can use the parameter `n` to represent a shift of n days.

\>>> from pandas.tseries.offsets import Day
\>>> ts \= pd.Timestamp(2022, 12, 9, 15)
\>>> ts
Timestamp('2022-12-09 15:00:00')

Copy to clipboard

\>>> ts + Day()
Timestamp('2022-12-10 15:00:00')
\>>> ts \- Day(4)
Timestamp('2022-12-05 15:00:00')

Copy to clipboard

\>>> ts + Day(\-4)
Timestamp('2022-12-05 15:00:00')

Copy to clipboard

On this page