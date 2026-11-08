[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.weekday.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.Week.weekday.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.weekday.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.Week.weekday.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.Week.weekday.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.Week.weekday.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.Week.weekday.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.Week.weekday.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.Week.weekday.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.Week.weekday.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.Week.weekday.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.Week.weekday.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.Week.weekday.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.Week.weekday.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.Week.weekday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.weekday.html#pandas-tseries-offsets-week-weekday "Link to this heading")

=========================================================================================================================================================================================

Week.weekday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.weekday.html#pandas.tseries.offsets.Week.weekday "Link to this definition")

Return the day of the week on which the offset is applied.

This is the weekday on which the weekly offset is anchored. The value is an integer representing the day of the week, where Monday is 0 and Sunday is 6, or None if no specific weekday is set.

See also

[`Week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.html#pandas.tseries.offsets.Week "pandas.tseries.offsets.Week")

The weekly offset class.

`tseries.offsets.WeekOfMonth`

Describes monthly dates like the Tuesday of the 2nd week of each month.

Examples

\>>> pd.offsets.Week(weekday\=0).weekday
0

Copy to clipboard

\>>> pd.offsets.Week(weekday\=6).weekday
6

Copy to clipboard

\>>> pd.offsets.Week().weekday is None
True

Copy to clipboard

On this page