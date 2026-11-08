[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_month_start.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.is\_month\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_month_start.html#pandas-datetimeindex-is-month-start "Link to this heading")

===========================================================================================================================================================================================

property DatetimeIndex.is\_month\_start[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L679-L700)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_month_start.html#pandas.DatetimeIndex.is_month_start "Link to this definition")

Indicates whether the date is the first day of the month.

This boolean attribute evaluates to True if the date falls on the first day of a calendar month, and False otherwise. If the index has a business `freq` (e.g. `"BMS"`), the result follows that frequency’s month boundaries instead of the calendar’s.

See also

[`DatetimeIndex.is_month_end`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_month_end.html#pandas.DatetimeIndex.is_month_end "pandas.DatetimeIndex.is_month_end")

Return a boolean indicating whether the date is the last day of the month.

Examples

\>>> idx \= pd.date\_range("2018-02-27", periods\=3)
\>>> idx.is\_month\_start
array(\[False, False,  True\])

Copy to clipboard

On this page