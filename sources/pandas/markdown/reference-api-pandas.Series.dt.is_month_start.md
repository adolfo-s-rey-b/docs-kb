[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_start.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.is_month_start.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_start.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.is_month_start.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.is_month_start.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.is_month_start.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.is_month_start.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.is_month_start.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.is_month_start.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.is_month_start.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.is_month_start.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.is_month_start.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.is_month_start.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.is_month_start.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.is\_month\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_start.html#pandas-series-dt-is-month-start "Link to this heading")

===============================================================================================================================================================================

Series.dt.is\_month\_start[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_start.html#pandas.Series.dt.is_month_start "Link to this definition")

Indicates whether the date is the first day of the month.

This boolean attribute evaluates to True if the date falls on the first day of a calendar month, and False otherwise.

Returns:

Series or array

For Series, returns a Series with boolean values. For DatetimeIndex, returns a boolean array.

See also

[`is_month_start`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_start.html#pandas.Series.dt.is_month_start "pandas.Series.dt.is_month_start")

Return a boolean indicating whether the date is the first day of the month.

[`is_month_end`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_end.html#pandas.Series.dt.is_month_end "pandas.Series.dt.is_month_end")

Return a boolean indicating whether the date is the last day of the month.

Examples

This method is available on Series with datetime values under the `.dt` accessor, and directly on DatetimeIndex.

\>>> s \= pd.Series(pd.date\_range("2018-02-27", periods\=3))
\>>> s
0   2018-02-27
1   2018-02-28
2   2018-03-01
dtype: datetime64\[us\]
\>>> s.dt.is\_month\_start
0    False
1    False
2    True
dtype: bool
\>>> s.dt.is\_month\_end
0    False
1    True
2    False
dtype: bool

Copy to clipboard

\>>> idx \= pd.date\_range("2018-02-27", periods\=3)
\>>> idx.is\_month\_start
array(\[False, False, True\])
\>>> idx.is\_month\_end
array(\[False, True, False\])

Copy to clipboard

On this page