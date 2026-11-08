[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_right.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.closed\_right[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_right.html#pandas-interval-closed-right "Link to this heading")

=====================================================================================================================================================================

Interval.closed\_right[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_right.html#pandas.Interval.closed_right "Link to this definition")

Check if the interval is closed on the right side.

For the meaning of closed and open see [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
.

Returns:

bool

True if the Interval is closed on the left-side.

See also

[`Interval.closed_left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_left.html#pandas.Interval.closed_left "pandas.Interval.closed_left")

Check if the interval is closed on the left side.

[`Interval.open_right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_right.html#pandas.Interval.open_right "pandas.Interval.open_right")

Boolean inverse of closed\_right.

Examples

\>>> iv \= pd.Interval(0, 5, closed\='both')
\>>> iv.closed\_right
True

Copy to clipboard

\>>> iv \= pd.Interval(0, 5, closed\='left')
\>>> iv.closed\_right
False

Copy to clipboard

On this page