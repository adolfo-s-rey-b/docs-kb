[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_leap_year.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.is_leap_year.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_leap_year.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.is_leap_year.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.is_leap_year.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.is_leap_year.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.is_leap_year.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.is_leap_year.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.is_leap_year.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.is_leap_year.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.is_leap_year.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.is_leap_year.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.is_leap_year.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.is_leap_year.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.is\_leap\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_leap_year.html#pandas-series-dt-is-leap-year "Link to this heading")

=========================================================================================================================================================================

Series.dt.is\_leap\_year[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_leap_year.html#pandas.Series.dt.is_leap_year "Link to this definition")

Boolean indicator if the date belongs to a leap year.

A leap year is a year, which has 366 days (instead of 365) including 29th of February as an intercalary day. Leap years are years which are multiples of four with the exception of years divisible by 100 but not by 400.

Returns:

Series or ndarray

Booleans indicating if dates belong to a leap year.

See also

[`DatetimeIndex.is_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_end.html#pandas.DatetimeIndex.is_year_end "pandas.DatetimeIndex.is_year_end")

Indicate whether the date is the last day of the year.

[`DatetimeIndex.is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_start.html#pandas.DatetimeIndex.is_year_start "pandas.DatetimeIndex.is_year_start")

Indicate whether the date is the first day of a year.

Examples

This method is available on Series with datetime values under the `.dt` accessor, and directly on DatetimeIndex.

\>>> idx \= pd.date\_range("2012-01-01", "2015-01-01", freq\="YE")
\>>> idx
DatetimeIndex(\['2012-12-31', '2013-12-31', '2014-12-31'\],
              dtype='datetime64\[us\]', freq='YE-DEC')
\>>> idx.is\_leap\_year
array(\[ True, False, False\])

Copy to clipboard

\>>> dates\_series \= pd.Series(idx)
\>>> dates\_series
0   2012-12-31
1   2013-12-31
2   2014-12-31
dtype: datetime64\[us\]
\>>> dates\_series.dt.is\_leap\_year
0     True
1    False
2    False
dtype: bool

Copy to clipboard

On this page