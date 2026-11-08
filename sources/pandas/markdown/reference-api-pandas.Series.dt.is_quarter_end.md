[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_end.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.is_quarter_end.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_end.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.is_quarter_end.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.is_quarter_end.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.is_quarter_end.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.is_quarter_end.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.is_quarter_end.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.is_quarter_end.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.is_quarter_end.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.is_quarter_end.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.is_quarter_end.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.is_quarter_end.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.is_quarter_end.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.is\_quarter\_end[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_end.html#pandas-series-dt-is-quarter-end "Link to this heading")

===============================================================================================================================================================================

Series.dt.is\_quarter\_end[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_end.html#pandas.Series.dt.is_quarter_end "Link to this definition")

Indicator for whether the date is the last day of a quarter.

This boolean attribute evaluates to True if the date falls on the last day of a calendar quarter (March 31, June 30, September 30, or December 31), and False otherwise.

Returns:

**is\_quarter\_end**Series or DatetimeIndex

The same type as the original data with boolean values. Series will have the same name and index. DatetimeIndex will have the same name.

See also

[`quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.quarter.html#pandas.Series.dt.quarter "pandas.Series.dt.quarter")

Return the quarter of the date.

[`is_quarter_start`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_start.html#pandas.Series.dt.is_quarter_start "pandas.Series.dt.is_quarter_start")

Similar property indicating the quarter start.

Examples

This method is available on Series with datetime values under the `.dt` accessor, and directly on DatetimeIndex.

\>>> df \= pd.DataFrame({'dates': pd.date\_range("2017-03-30",
...                    periods\=4)})
\>>> df.assign(quarter\=df.dates.dt.quarter,
...           is\_quarter\_end\=df.dates.dt.is\_quarter\_end)
       dates  quarter    is\_quarter\_end
0 2017-03-30        1             False
1 2017-03-31        1              True
2 2017-04-01        2             False
3 2017-04-02        2             False

Copy to clipboard

\>>> idx \= pd.date\_range('2017-03-30', periods\=4)
\>>> idx
DatetimeIndex(\['2017-03-30', '2017-03-31', '2017-04-01', '2017-04-02'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

\>>> idx.is\_quarter\_end
array(\[False,  True, False, False\])

Copy to clipboard

On this page