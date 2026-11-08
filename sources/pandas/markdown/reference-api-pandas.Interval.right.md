[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.right.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Interval.right.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Interval.right.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Interval.right.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Interval.right.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Interval.right.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Interval.right.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Interval.right.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Interval.right.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Interval.right.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Interval.right.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Interval.right.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Interval.right.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Interval.right.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.right[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.right.html#pandas-interval-right "Link to this heading")

===============================================================================================================================================

Interval.right[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.right.html#pandas.Interval.right "Link to this definition")

Right bound for the interval.

The right endpoint of the interval. Whether it is included in the interval depends on the value of [`closed`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed.html#pandas.Interval.closed "pandas.Interval.closed")
.

See also

[`Interval.left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.left.html#pandas.Interval.left "pandas.Interval.left")

Return the left bound for the interval.

`numpy.ndarray.right`

A similar method in numpy for obtaining the right endpoint(s) of intervals.

Examples

\>>> interval \= pd.Interval(left\=1, right\=2, closed\='left')
\>>> interval
Interval(1, 2, closed='left')
\>>> interval.right
2

Copy to clipboard

On this page