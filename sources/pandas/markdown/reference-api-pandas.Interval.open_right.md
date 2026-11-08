[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_right.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Interval.open_right.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_right.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Interval.open_right.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Interval.open_right.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Interval.open_right.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Interval.open_right.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Interval.open_right.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Interval.open_right.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Interval.open_right.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Interval.open_right.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Interval.open_right.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Interval.open_right.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Interval.open_right.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.open\_right[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_right.html#pandas-interval-open-right "Link to this heading")

===============================================================================================================================================================

Interval.open\_right[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_right.html#pandas.Interval.open_right "Link to this definition")

Check if the interval is open on the right side.

For the meaning of closed and open see [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
.

Returns:

bool

True if the Interval is not closed on the left-side.

See also

[`Interval.open_left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_left.html#pandas.Interval.open_left "pandas.Interval.open_left")

Check if the interval is open on the left side.

[`Interval.closed_right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_right.html#pandas.Interval.closed_right "pandas.Interval.closed_right")

Boolean inverse of open\_right.

Examples

\>>> iv \= pd.Interval(0, 5, closed\='left')
\>>> iv.open\_right
True

Copy to clipboard

\>>> iv \= pd.Interval(0, 5)
\>>> iv.open\_right
False

Copy to clipboard

On this page