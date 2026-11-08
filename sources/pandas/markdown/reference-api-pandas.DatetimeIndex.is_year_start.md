[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_start.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.is_year_start.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_start.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.is_year_start.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.is_year_start.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.is_year_start.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.is_year_start.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.is_year_start.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.is_year_start.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.is_year_start.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.is_year_start.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.is_year_start.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.is_year_start.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.is_year_start.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.is\_year\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_start.html#pandas-datetimeindex-is-year-start "Link to this heading")

========================================================================================================================================================================================

property DatetimeIndex.is\_year\_start[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L777-L809)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_start.html#pandas.DatetimeIndex.is_year_start "Link to this definition")

Indicate whether the date is the first day of a year.

This boolean attribute evaluates to True if the date is January 1st, and False otherwise. If the index has a business or anchored `freq` (e.g. `"BYS"` or `"YS-APR"`), the result follows that frequency’s year boundaries instead of the calendar’s.

See also

[`DatetimeIndex.is_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_end.html#pandas.DatetimeIndex.is_year_end "pandas.DatetimeIndex.is_year_end")

Similar property indicating the last day of the year.

Examples

\>>> idx \= pd.date\_range("2017-12-30", periods\=3)
\>>> idx.is\_year\_start
array(\[False, False,  True\])

Copy to clipboard

With a business `freq`, the first business day of the year counts as the year start even when it is not January 1st:

\>>> idx \= pd.date\_range("2020-10-30", periods\=4, freq\="BYS")
\>>> idx
DatetimeIndex(\['2021-01-01', '2022-01-03', '2023-01-02', '2024-01-01'\],
              dtype='datetime64\[us\]', freq='BYS-JAN')
\>>> idx.is\_year\_start
array(\[ True,  True,  True,  True\])

Copy to clipboard

On this page