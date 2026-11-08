[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.minute.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.minute.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.minute.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.minute.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.minute.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.minute.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.minute.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.minute.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.minute.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.minute.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.minute.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.minute.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.minute.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.minute.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.minute[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.minute.html#pandas-periodindex-minute "Link to this heading")

===========================================================================================================================================================

property PeriodIndex.minute[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L454-L475)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.minute.html#pandas.PeriodIndex.minute "Link to this definition")

The minute of the period.

Returns the minute component for each period in the index.

See also

[`PeriodIndex.hour`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.hour.html#pandas.PeriodIndex.hour "pandas.PeriodIndex.hour")

The hour of the period.

[`PeriodIndex.second`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.second.html#pandas.PeriodIndex.second "pandas.PeriodIndex.second")

The second of the period.

[`PeriodIndex.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas.PeriodIndex.to_timestamp "pandas.PeriodIndex.to_timestamp")

Cast to DatetimeArray/Index.

Examples

\>>> idx \= pd.PeriodIndex(
...     \["2023-01-01 10:30:00", "2023-01-01 11:50:00"\], freq\="min"
... )
\>>> idx.minute
Index(\[30, 50\], dtype='int64')

Copy to clipboard

On this page