[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_right.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.closed_right.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_right.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.closed_right.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.closed_right.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.closed_right.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.closed_right.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.closed_right.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.closed_right.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.closed_right.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.closed_right.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.closed_right.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.closed_right.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.closed_right.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.closed\_right[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_right.html#pandas-intervalindex-closed-right "Link to this heading")

====================================================================================================================================================================================

property IntervalIndex.closed\_right[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L323-L347)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_right.html#pandas.IntervalIndex.closed_right "Link to this definition")

Check if the intervals are closed on the right side.

All intervals in an IntervalIndex share the same `closed` value, so this describes the index as a whole rather than element-wise.

See also

[`IntervalIndex.closed_left`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_left.html#pandas.IntervalIndex.closed_left "pandas.IntervalIndex.closed_left")

Check if the intervals are closed on the left side.

[`IntervalIndex.open_right`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.open_right.html#pandas.IntervalIndex.open_right "pandas.IntervalIndex.open_right")

Boolean inverse of closed\_right.

Examples

\>>> iv\_idx \= pd.interval\_range(start\=0, end\=2, closed\="right")
\>>> iv\_idx.closed\_right
True

Copy to clipboard

\>>> iv\_idx \= pd.interval\_range(start\=0, end\=2, closed\="left")
\>>> iv\_idx.closed\_right
False

Copy to clipboard

On this page