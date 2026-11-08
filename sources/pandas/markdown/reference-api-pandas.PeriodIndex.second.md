[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.second.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.second[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.second.html#pandas-periodindex-second "Link to this heading")

===========================================================================================================================================================

property PeriodIndex.second[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L477-L498)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.second.html#pandas.PeriodIndex.second "Link to this definition")

The second of the period.

Returns the second component for each period in the index.

See also

[`PeriodIndex.hour`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.hour.html#pandas.PeriodIndex.hour "pandas.PeriodIndex.hour")

The hour of the period.

[`PeriodIndex.minute`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.minute.html#pandas.PeriodIndex.minute "pandas.PeriodIndex.minute")

The minute of the period.

[`PeriodIndex.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas.PeriodIndex.to_timestamp "pandas.PeriodIndex.to_timestamp")

Cast to DatetimeArray/Index.

Examples

\>>> idx \= pd.PeriodIndex(
...     \["2023-01-01 10:00:30", "2023-01-01 10:00:31"\], freq\="s"
... )
\>>> idx.second
Index(\[30, 31\], dtype='int64')

Copy to clipboard

On this page