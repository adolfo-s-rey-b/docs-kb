[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_left.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Interval.open_left.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_left.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Interval.open_left.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Interval.open_left.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Interval.open_left.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Interval.open_left.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Interval.open_left.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Interval.open_left.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Interval.open_left.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Interval.open_left.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Interval.open_left.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Interval.open_left.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Interval.open_left.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.open\_left[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_left.html#pandas-interval-open-left "Link to this heading")

============================================================================================================================================================

Interval.open\_left[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_left.html#pandas.Interval.open_left "Link to this definition")

Check if the interval is open on the left side.

For the meaning of closed and open see [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
.

Returns:

bool

True if the Interval is not closed on the left-side.

See also

[`Interval.open_right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_right.html#pandas.Interval.open_right "pandas.Interval.open_right")

Check if the interval is open on the right side.

[`Interval.closed_left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_left.html#pandas.Interval.closed_left "pandas.Interval.closed_left")

Boolean inverse of open\_left.

Examples

\>>> iv \= pd.Interval(0, 5, closed\='neither')
\>>> iv.open\_left
True

Copy to clipboard

\>>> iv \= pd.Interval(0, 5, closed\='both')
\>>> iv.open\_left
False

Copy to clipboard

On this page