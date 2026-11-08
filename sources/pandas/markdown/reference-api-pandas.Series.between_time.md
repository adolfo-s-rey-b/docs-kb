[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.between_time.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.between_time.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.between_time.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.between_time.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.between_time.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.between_time.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.between_time.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.between_time.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.between_time.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.between_time.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.between_time.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.between_time.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.between_time.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.between_time.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.between\_time[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.between_time.html#pandas-series-between-time "Link to this heading")

===============================================================================================================================================================

Series.between\_time(_start\_time_, _end\_time_, _inclusive\='both'_, _axis\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L9307-L9388)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.between_time.html#pandas.Series.between_time "Link to this definition")

Select values between particular times of the day (e.g., 9:00-9:30 AM).

By setting `start_time` to be later than `end_time`, you can get the times that are _not_ between the two times.

Parameters:

**start\_time**datetime.time or str

Initial time as a time filter limit.

**end\_time**datetime.time or str

End time as a time filter limit.

**inclusive**{“both”, “neither”, “left”, “right”}, default “both”

Include boundaries; whether to set each bound as closed or open.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Determine range time on index or columns value. For Series this parameter is unused and defaults to 0.

Returns:

Series or DataFrame

Data from the original object filtered to the specified dates range.

Raises:

TypeError

If the index is not a [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")

See also

[`at_time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.at_time.html#pandas.Series.at_time "pandas.Series.at_time")

Select values at a particular time of the day.

[`DatetimeIndex.indexer_between_time`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_between_time.html#pandas.DatetimeIndex.indexer_between_time "pandas.DatetimeIndex.indexer_between_time")

Get just the index locations for values between particular times of the day.

Examples

\>>> i \= pd.date\_range("2018-04-09", periods\=4, freq\="1D20min")
\>>> ts \= pd.DataFrame({"A": \[1, 2, 3, 4\]}, index\=i)
\>>> ts
                     A
2018-04-09 00:00:00  1
2018-04-10 00:20:00  2
2018-04-11 00:40:00  3
2018-04-12 01:00:00  4

Copy to clipboard

\>>> ts.between\_time("0:15", "0:45")
                     A
2018-04-10 00:20:00  2
2018-04-11 00:40:00  3

Copy to clipboard

You get the times that are _not_ between two times by setting `start_time` later than `end_time`:

\>>> ts.between\_time("0:45", "0:15")
                     A
2018-04-09 00:00:00  1
2018-04-12 01:00:00  4

Copy to clipboard

On this page