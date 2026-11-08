[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_leap_year.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.is\_leap\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_leap_year.html#pandas-timestamp-is-leap-year "Link to this heading")

=========================================================================================================================================================================

Timestamp.is\_leap\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_leap_year.html#pandas.Timestamp.is_leap_year "Link to this definition")

Return True if year is a leap year.

A leap year is a year, which has 366 days (instead of 365) including 29th of February as an intercalary day. Leap years are years which are multiples of four with the exception of years divisible by 100 but not by 400.

Returns:

bool

True if year is a leap year, else False

See also

[`Period.is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.is_leap_year.html#pandas.Period.is_leap_year "pandas.Period.is_leap_year")

Return True if the period’s year is in a leap year.

[`DatetimeIndex.is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_leap_year.html#pandas.DatetimeIndex.is_leap_year "pandas.DatetimeIndex.is_leap_year")

Boolean indicator if the date belongs to a leap year.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14)
\>>> ts.is\_leap\_year
True

Copy to clipboard

On this page