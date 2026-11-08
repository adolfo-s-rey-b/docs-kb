[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_left.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.closed\_left[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_left.html#pandas-interval-closed-left "Link to this heading")

==================================================================================================================================================================

Interval.closed\_left[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_left.html#pandas.Interval.closed_left "Link to this definition")

Check if the interval is closed on the left side.

For the meaning of closed and open see [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
.

Returns:

bool

True if the Interval is closed on the left-side.

See also

[`Interval.closed_right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_right.html#pandas.Interval.closed_right "pandas.Interval.closed_right")

Check if the interval is closed on the right side.

[`Interval.open_left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_left.html#pandas.Interval.open_left "pandas.Interval.open_left")

Boolean inverse of closed\_left.

Examples

\>>> iv \= pd.Interval(0, 5, closed\='left')
\>>> iv.closed\_left
True

Copy to clipboard

\>>> iv \= pd.Interval(0, 5, closed\='right')
\>>> iv.closed\_left
False

Copy to clipboard

On this page