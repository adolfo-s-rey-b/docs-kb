[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_start.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.is_quarter_start.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.is_quarter_start.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.is\_quarter\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_start.html#pandas-datetimeindex-is-quarter-start "Link to this heading")

=================================================================================================================================================================================================

property DatetimeIndex.is\_quarter\_start[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L725-L749)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_start.html#pandas.DatetimeIndex.is_quarter_start "Link to this definition")

Indicator for whether the date is the first day of a quarter.

This boolean attribute evaluates to True if the date falls on the first day of a calendar quarter (January 1, April 1, July 1, or October 1), and False otherwise. If the index has a business or anchored `freq` (e.g. `"BQS"` or `"QS-FEB"`), the result follows that frequency’s quarter boundaries instead of the calendar’s.

See also

[`DatetimeIndex.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.quarter.html#pandas.DatetimeIndex.quarter "pandas.DatetimeIndex.quarter")

Return the quarter of the date.

[`DatetimeIndex.is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_end.html#pandas.DatetimeIndex.is_quarter_end "pandas.DatetimeIndex.is_quarter_end")

Similar property for indicating the quarter end.

Examples

\>>> idx \= pd.date\_range("2017-03-30", periods\=4)
\>>> idx.is\_quarter\_start
array(\[False, False,  True, False\])

Copy to clipboard

On this page