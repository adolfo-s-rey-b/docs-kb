[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_non_overlapping_monotonic.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.is\_non\_overlapping\_monotonic[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_non_overlapping_monotonic.html#pandas-intervalindex-is-non-overlapping-monotonic "Link to this heading")

======================================================================================================================================================================================================================================

IntervalIndex.is\_non\_overlapping\_monotonic[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L266-L295)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_non_overlapping_monotonic.html#pandas.IntervalIndex.is_non_overlapping_monotonic "Link to this definition")

Return True if the IntervalIndex is non-overlapping and monotonic.

Non-overlapping means no Intervals share points, and monotonic means either monotonic increasing or monotonic decreasing.

See also

[`IntervalIndex.overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.overlaps.html#pandas.IntervalIndex.overlaps "pandas.IntervalIndex.overlaps")

Check an IntervalIndex elementwise for overlaps.

[`IntervalIndex.is_overlapping`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_overlapping.html#pandas.IntervalIndex.is_overlapping "pandas.IntervalIndex.is_overlapping")

Return True if the IntervalIndex has overlapping intervals.

Examples

\>>> interv\_idx \= pd.interval\_range(start\=0, end\=2)
\>>> interv\_idx
IntervalIndex(\[(0, 1\], (1, 2\]\], dtype='interval\[int64, right\]')
\>>> interv\_idx.is\_non\_overlapping\_monotonic
True

Copy to clipboard

\>>> interv\_idx \= pd.interval\_range(start\=0, end\=2, closed\="both")
\>>> interv\_idx
IntervalIndex(\[\[0, 1\], \[1, 2\]\], dtype='interval\[int64, both\]')
\>>> interv\_idx.is\_non\_overlapping\_monotonic
False

Copy to clipboard

On this page