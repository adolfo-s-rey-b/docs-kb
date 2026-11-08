[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.at_time.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.at_time.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.at_time.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.at_time.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.at_time.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.at_time.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.at_time.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.at_time.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.at_time.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.at_time.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.at_time.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.at_time.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.at_time.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.at_time.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.at\_time[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.at_time.html#pandas-series-at-time "Link to this heading")

================================================================================================================================================

Series.at\_time(_time_, _asof\=False_, _axis\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L9246-L9305)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.at_time.html#pandas.Series.at_time "Link to this definition")

Select values at particular time of day (e.g., 9:30AM).

This method filters rows whose index has a time component matching the specified time. The index must be a DatetimeIndex.

Parameters:

**time**datetime.time or str

The values to select.

**asof**bool, default False

This parameter is currently not supported.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

For Series this parameter is unused and defaults to 0.

Returns:

Series or DataFrame

The values with the specified time.

Raises:

TypeError

If the index is not a [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")

See also

[`between_time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.between_time.html#pandas.Series.between_time "pandas.Series.between_time")

Select values between particular times of the day.

[`DatetimeIndex.indexer_at_time`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_at_time.html#pandas.DatetimeIndex.indexer_at_time "pandas.DatetimeIndex.indexer_at_time")

Get just the index locations for values at particular time of the day.

Examples

\>>> i \= pd.date\_range("2018-04-09", periods\=4, freq\="12h")
\>>> ts \= pd.DataFrame({"A": \[1, 2, 3, 4\]}, index\=i)
\>>> ts
                     A
2018-04-09 00:00:00  1
2018-04-09 12:00:00  2
2018-04-10 00:00:00  3
2018-04-10 12:00:00  4

Copy to clipboard

\>>> ts.at\_time("12:00")
                     A
2018-04-09 12:00:00  2
2018-04-10 12:00:00  4

Copy to clipboard

On this page