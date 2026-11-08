[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.closed[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed.html#pandas-interval-closed "Link to this heading")

==================================================================================================================================================

Interval.closed[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed.html#pandas.Interval.closed "Link to this definition")

String describing the inclusive side the intervals.

Either `left`, `right`, `both` or `neither`.

See also

[`Interval.closed_left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_left.html#pandas.Interval.closed_left "pandas.Interval.closed_left")

Check if the interval is closed on the left side.

[`Interval.closed_right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_right.html#pandas.Interval.closed_right "pandas.Interval.closed_right")

Check if the interval is closed on the right side.

[`Interval.open_left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_left.html#pandas.Interval.open_left "pandas.Interval.open_left")

Check if the interval is open on the left side.

[`Interval.open_right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_right.html#pandas.Interval.open_right "pandas.Interval.open_right")

Check if the interval is open on the right side.

Examples

\>>> interval \= pd.Interval(left\=1, right\=2, closed\='left')
\>>> interval
Interval(1, 2, closed='left')
\>>> interval.closed
'left'

Copy to clipboard

On this page