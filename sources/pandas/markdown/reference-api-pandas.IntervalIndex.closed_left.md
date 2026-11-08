[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_left.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.closed\_left[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_left.html#pandas-intervalindex-closed-left "Link to this heading")

=================================================================================================================================================================================

property IntervalIndex.closed\_left[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L297-L321)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_left.html#pandas.IntervalIndex.closed_left "Link to this definition")

Check if the intervals are closed on the left side.

All intervals in an IntervalIndex share the same `closed` value, so this describes the index as a whole rather than element-wise.

See also

[`IntervalIndex.closed_right`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_right.html#pandas.IntervalIndex.closed_right "pandas.IntervalIndex.closed_right")

Check if the intervals are closed on the right side.

[`IntervalIndex.open_left`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.open_left.html#pandas.IntervalIndex.open_left "pandas.IntervalIndex.open_left")

Boolean inverse of closed\_left.

Examples

\>>> iv\_idx \= pd.interval\_range(start\=0, end\=2, closed\="left")
\>>> iv\_idx.closed\_left
True

Copy to clipboard

\>>> iv\_idx \= pd.interval\_range(start\=0, end\=2, closed\="right")
\>>> iv\_idx.closed\_left
False

Copy to clipboard

On this page