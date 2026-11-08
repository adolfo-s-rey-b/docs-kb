[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_leap_year.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.is\_leap\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_leap_year.html#pandas-datetimeindex-is-leap-year "Link to this heading")

=====================================================================================================================================================================================

property DatetimeIndex.is\_leap\_year[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L835-L858)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_leap_year.html#pandas.DatetimeIndex.is_leap_year "Link to this definition")

Boolean indicator if the date belongs to a leap year.

A leap year is a year, which has 366 days (instead of 365) including 29th of February as an intercalary day. Leap years are years which are multiples of four with the exception of years divisible by 100 but not by 400.

See also

[`DatetimeIndex.is_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_end.html#pandas.DatetimeIndex.is_year_end "pandas.DatetimeIndex.is_year_end")

Indicate whether the date is the last day of the year.

[`DatetimeIndex.is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_start.html#pandas.DatetimeIndex.is_year_start "pandas.DatetimeIndex.is_year_start")

Indicate whether the date is the first day of a year.

Examples

\>>> idx \= pd.date\_range("2012-01-01", "2015-01-01", freq\="YE")
\>>> idx.is\_leap\_year
array(\[ True, False, False\])

Copy to clipboard

On this page