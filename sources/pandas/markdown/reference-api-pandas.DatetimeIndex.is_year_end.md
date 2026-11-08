[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_end.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.is_year_end.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_end.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.is_year_end.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.is_year_end.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.is_year_end.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.is_year_end.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.is_year_end.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.is_year_end.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.is_year_end.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.is_year_end.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.is_year_end.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.is_year_end.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.is_year_end.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.is\_year\_end[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_end.html#pandas-datetimeindex-is-year-end "Link to this heading")

==================================================================================================================================================================================

property DatetimeIndex.is\_year\_end[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L811-L833)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_end.html#pandas.DatetimeIndex.is_year_end "Link to this definition")

Indicate whether the date is the last day of the year.

This boolean attribute evaluates to True if the date is December 31st, and False otherwise. If the index has a business or anchored `freq` (e.g. `"BYE"` or `"YE-MAR"`), the result follows that frequency’s year boundaries instead of the calendar’s.

See also

[`DatetimeIndex.is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_start.html#pandas.DatetimeIndex.is_year_start "pandas.DatetimeIndex.is_year_start")

Similar property indicating the start of the year.

Examples

\>>> idx \= pd.date\_range("2017-12-30", periods\=3)
\>>> idx.is\_year\_end
array(\[False,  True, False\])

Copy to clipboard

On this page