[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_start.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.is_year_start.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_start.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.is_year_start.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.is_year_start.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.is_year_start.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.is_year_start.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.is_year_start.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.is_year_start.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.is_year_start.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.is_year_start.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.is_year_start.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.is_year_start.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.is_year_start.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.is\_year\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_start.html#pandas-series-dt-is-year-start "Link to this heading")

============================================================================================================================================================================

Series.dt.is\_year\_start[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_start.html#pandas.Series.dt.is_year_start "Link to this definition")

Indicate whether the date is the first day of a year.

This boolean attribute evaluates to True if the date is January 1st, and False otherwise.

Returns:

Series or DatetimeIndex

The same type as the original data with boolean values. Series will have the same name and index. DatetimeIndex will have the same name.

See also

[`is_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_end.html#pandas.Series.dt.is_year_end "pandas.Series.dt.is_year_end")

Similar property indicating the last day of the year.

Examples

This method is available on Series with datetime values under the `.dt` accessor, and directly on DatetimeIndex.

\>>> dates \= pd.Series(pd.date\_range("2017-12-30", periods\=3))
\>>> dates
0   2017-12-30
1   2017-12-31
2   2018-01-01
dtype: datetime64\[us\]

Copy to clipboard

\>>> dates.dt.is\_year\_start
0    False
1    False
2    True
dtype: bool

Copy to clipboard

\>>> idx \= pd.date\_range("2017-12-30", periods\=3)
\>>> idx
DatetimeIndex(\['2017-12-30', '2017-12-31', '2018-01-01'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

\>>> idx.is\_year\_start
array(\[False, False,  True\])

Copy to clipboard

This method, when applied to Series with datetime values under the `.dt` accessor, will lose information about Business offsets.

\>>> dates \= pd.Series(pd.date\_range("2020-10-30", periods\=4, freq\="BYS"))
\>>> dates
0   2021-01-01
1   2022-01-03
2   2023-01-02
3   2024-01-01
dtype: datetime64\[us\]

Copy to clipboard

\>>> dates.dt.is\_year\_start
0    True
1    False
2    False
3    True
dtype: bool

Copy to clipboard

\>>> idx \= pd.date\_range("2020-10-30", periods\=4, freq\="BYS")
\>>> idx
DatetimeIndex(\['2021-01-01', '2022-01-03', '2023-01-02', '2024-01-01'\],
              dtype='datetime64\[us\]', freq='BYS-JAN')

Copy to clipboard

\>>> idx.is\_year\_start
array(\[ True,  True,  True,  True\])

Copy to clipboard

On this page