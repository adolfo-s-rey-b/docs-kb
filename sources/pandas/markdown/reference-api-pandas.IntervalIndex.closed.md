[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.closed.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.closed.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.closed.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.closed.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.closed.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.closed.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.closed.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.closed.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.closed.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.closed.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.closed.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.closed.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.closed[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed.html#pandas-intervalindex-closed "Link to this heading")

=================================================================================================================================================================

IntervalIndex.closed[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L243-L264)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed.html#pandas.IntervalIndex.closed "Link to this definition")

String describing the inclusive side of the intervals.

Either `left`, `right`, `both` or `neither`.

See also

[`IntervalIndex.set_closed`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.set_closed.html#pandas.IntervalIndex.set_closed "pandas.IntervalIndex.set_closed")

Return an IntervalIndex identical to the current one, but closed on the specified side.

[`Interval.closed`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed.html#pandas.Interval.closed "pandas.Interval.closed")

Returns inclusive side of the Interval.

Examples

\>>> interv\_idx \= pd.interval\_range(start\=0, end\=2)
\>>> interv\_idx
IntervalIndex(\[(0, 1\], (1, 2\]\], dtype='interval\[int64, right\]')
\>>> interv\_idx.closed
'right'

Copy to clipboard

On this page