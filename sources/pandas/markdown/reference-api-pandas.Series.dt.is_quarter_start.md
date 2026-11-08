[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_start.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.is_quarter_start.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_start.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.is_quarter_start.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.is_quarter_start.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.is_quarter_start.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.is_quarter_start.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.is_quarter_start.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.is_quarter_start.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.is_quarter_start.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.is_quarter_start.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.is_quarter_start.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.is_quarter_start.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.is_quarter_start.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.is\_quarter\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_start.html#pandas-series-dt-is-quarter-start "Link to this heading")

=====================================================================================================================================================================================

Series.dt.is\_quarter\_start[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_start.html#pandas.Series.dt.is_quarter_start "Link to this definition")

Indicator for whether the date is the first day of a quarter.

This boolean attribute evaluates to True if the date falls on the first day of a calendar quarter (January 1, April 1, July 1, or October 1), and False otherwise.

Returns:

**is\_quarter\_start**Series or DatetimeIndex

The same type as the original data with boolean values. Series will have the same name and index. DatetimeIndex will have the same name.

See also

[`quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.quarter.html#pandas.Series.dt.quarter "pandas.Series.dt.quarter")

Return the quarter of the date.

[`is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_end.html#pandas.Series.dt.is_quarter_end "pandas.Series.dt.is_quarter_end")

Similar property for indicating the quarter end.

Examples

This method is available on Series with datetime values under the `.dt` accessor, and directly on DatetimeIndex.

\>>> df \= pd.DataFrame({'dates': pd.date\_range("2017-03-30",
...                   periods\=4)})
\>>> df.assign(quarter\=df.dates.dt.quarter,
...           is\_quarter\_start\=df.dates.dt.is\_quarter\_start)
       dates  quarter  is\_quarter\_start
0 2017-03-30        1             False
1 2017-03-31        1             False
2 2017-04-01        2              True
3 2017-04-02        2             False

Copy to clipboard

\>>> idx \= pd.date\_range('2017-03-30', periods\=4)
\>>> idx
DatetimeIndex(\['2017-03-30', '2017-03-31', '2017-04-01', '2017-04-02'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

\>>> idx.is\_quarter\_start
array(\[False, False,  True, False\])

Copy to clipboard

On this page