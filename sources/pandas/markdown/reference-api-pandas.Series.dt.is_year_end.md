[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_end.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.is\_year\_end[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_end.html#pandas-series-dt-is-year-end "Link to this heading")

======================================================================================================================================================================

Series.dt.is\_year\_end[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_end.html#pandas.Series.dt.is_year_end "Link to this definition")

Indicate whether the date is the last day of the year.

This boolean attribute evaluates to True if the date is December 31st, and False otherwise.

Returns:

Series or DatetimeIndex

The same type as the original data with boolean values. Series will have the same name and index. DatetimeIndex will have the same name.

See also

[`is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_start.html#pandas.Series.dt.is_year_start "pandas.Series.dt.is_year_start")

Similar property indicating the start of the year.

Examples

This method is available on Series with datetime values under the `.dt` accessor, and directly on DatetimeIndex.

\>>> dates \= pd.Series(pd.date\_range("2017-12-30", periods\=3))
\>>> dates
0   2017-12-30
1   2017-12-31
2   2018-01-01
dtype: datetime64\[us\]

Copy to clipboard

\>>> dates.dt.is\_year\_end
0    False
1     True
2    False
dtype: bool

Copy to clipboard

\>>> idx \= pd.date\_range("2017-12-30", periods\=3)
\>>> idx
DatetimeIndex(\['2017-12-30', '2017-12-31', '2018-01-01'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

\>>> idx.is\_year\_end
array(\[False,  True, False\])

Copy to clipboard

On this page