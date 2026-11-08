[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_end.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.is\_quarter\_end[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_end.html#pandas-datetimeindex-is-quarter-end "Link to this heading")

===========================================================================================================================================================================================

property DatetimeIndex.is\_quarter\_end[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L751-L775)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_end.html#pandas.DatetimeIndex.is_quarter_end "Link to this definition")

Indicator for whether the date is the last day of a quarter.

This boolean attribute evaluates to True if the date falls on the last day of a calendar quarter (March 31, June 30, September 30, or December 31), and False otherwise. If the index has a business or anchored `freq` (e.g. `"BQE"` or `"QE-NOV"`), the result follows that frequency’s quarter boundaries instead of the calendar’s.

See also

[`DatetimeIndex.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.quarter.html#pandas.DatetimeIndex.quarter "pandas.DatetimeIndex.quarter")

Return the quarter of the date.

[`DatetimeIndex.is_quarter_start`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_start.html#pandas.DatetimeIndex.is_quarter_start "pandas.DatetimeIndex.is_quarter_start")

Similar property indicating the quarter start.

Examples

\>>> idx \= pd.date\_range("2017-03-30", periods\=4)
\>>> idx.is\_quarter\_end
array(\[False,  True, False, False\])

Copy to clipboard

On this page