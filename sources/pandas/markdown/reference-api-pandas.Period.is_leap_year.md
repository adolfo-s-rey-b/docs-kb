[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.is_leap_year.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.is_leap_year.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.is_leap_year.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.is_leap_year.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.is_leap_year.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.is_leap_year.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.is_leap_year.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.is_leap_year.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.is_leap_year.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.is_leap_year.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.is_leap_year.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.is_leap_year.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.is_leap_year.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.is_leap_year.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.is\_leap\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.is_leap_year.html#pandas-period-is-leap-year "Link to this heading")

================================================================================================================================================================

Period.is\_leap\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.is_leap_year.html#pandas.Period.is_leap_year "Link to this definition")

Return True if the period’s year is in a leap year.

A leap year is a year with 366 days (instead of 365), including February 29 as an intercalary day. Leap years are years divisible by 4, except for years divisible by 100 but not by 400.

See also

[`Timestamp.is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_leap_year.html#pandas.Timestamp.is_leap_year "pandas.Timestamp.is_leap_year")

Check if the year in a Timestamp is a leap year.

[`DatetimeIndex.is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_leap_year.html#pandas.DatetimeIndex.is_leap_year "pandas.DatetimeIndex.is_leap_year")

Boolean indicator if the date belongs to a leap year.

Examples

\>>> period \= pd.Period('2022-01', 'M')
\>>> period.is\_leap\_year
False

Copy to clipboard

\>>> period \= pd.Period('2020-01', 'M')
\>>> period.is\_leap\_year
True

Copy to clipboard

On this page