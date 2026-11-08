[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.open_right.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.open_right.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.open_right.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.open_right.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.open_right.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.open_right.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.open_right.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.open_right.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.open_right.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.open_right.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.open_right.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.open_right.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.open_right.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.open_right.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.open\_right[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.open_right.html#pandas-intervalindex-open-right "Link to this heading")

==============================================================================================================================================================================

property IntervalIndex.open\_right[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L375-L399)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.open_right.html#pandas.IntervalIndex.open_right "Link to this definition")

Check if the intervals are open on the right side.

All intervals in an IntervalIndex share the same `closed` value, so this describes the index as a whole rather than element-wise.

See also

[`IntervalIndex.open_left`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.open_left.html#pandas.IntervalIndex.open_left "pandas.IntervalIndex.open_left")

Check if the intervals are open on the left side.

[`IntervalIndex.closed_right`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_right.html#pandas.IntervalIndex.closed_right "pandas.IntervalIndex.closed_right")

Boolean inverse of open\_right.

Examples

\>>> iv\_idx \= pd.interval\_range(start\=0, end\=2, closed\="right")
\>>> iv\_idx.open\_right
False

Copy to clipboard

\>>> iv\_idx \= pd.interval\_range(start\=0, end\=2, closed\="left")
\>>> iv\_idx.open\_right
True

Copy to clipboard

On this page