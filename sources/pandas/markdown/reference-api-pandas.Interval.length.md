[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Interval.length.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Interval.length.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Interval.length.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Interval.length.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Interval.length.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Interval.length.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Interval.length.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Interval.length.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Interval.length.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Interval.length.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Interval.length.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Interval.length.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Interval.length.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Interval.length.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Interval.length[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.length.html#pandas-interval-length "Link to this heading")

==================================================================================================================================================

Interval.length[#](https://pandas.pydata.org/docs/reference/api/pandas.Interval.length.html#pandas.Interval.length "Link to this definition")

Return the length of the Interval.

The length is the distance between the right and left bounds, i.e. `right - left`. For time-like bounds this returns a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
 or [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")
.

See also

[`Interval.is_empty`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.is_empty.html#pandas.Interval.is_empty "pandas.Interval.is_empty")

Indicates if an interval contains no points.

Examples

\>>> interval \= pd.Interval(left\=1, right\=2, closed\='left')
\>>> interval
Interval(1, 2, closed='left')
\>>> interval.length
1

Copy to clipboard

On this page