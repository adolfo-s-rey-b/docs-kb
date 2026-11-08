[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.left.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.left[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.left.html#pandas-interval-left "Link to this heading")

============================================================================================================================================

Interval.left[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.left.html#pandas.Interval.left "Link to this definition")

Left bound for the interval.

The left endpoint of the interval. Whether it is included in the interval depends on the value of [`closed`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed.html#pandas.Interval.closed "pandas.Interval.closed")
.

See also

[`Interval.right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.right.html#pandas.Interval.right "pandas.Interval.right")

Return the right bound for the interval.

`numpy.ndarray.left`

A similar method in numpy for obtaining the left endpoint(s) of intervals.

Examples

\>>> interval \= pd.Interval(left\=1, right\=2, closed\='left')
\>>> interval
Interval(1, 2, closed='left')
\>>> interval.left
1

Copy to clipboard

On this page