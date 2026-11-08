[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.stop.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.RangeIndex.stop.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.stop.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.RangeIndex.stop.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.RangeIndex.stop.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.RangeIndex.stop.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.RangeIndex.stop.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.RangeIndex.stop.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.RangeIndex.stop.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.RangeIndex.stop.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.RangeIndex.stop.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.RangeIndex.stop.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.RangeIndex.stop.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.RangeIndex.stop.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.RangeIndex.stop[#](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.stop.html#pandas-rangeindex-stop "Link to this heading")

==================================================================================================================================================

property RangeIndex.stop[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/range.py#L363-L389)
[#](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.stop.html#pandas.RangeIndex.stop "Link to this definition")

The value of the stop parameter.

This property returns the stop value of the RangeIndex, which defines the upper (or lower, in case of negative steps) bound of the index range. The stop value is exclusive, meaning the RangeIndex includes values up to but not including this value.

See also

[`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")

Immutable index representing a range of integers.

[`RangeIndex.start`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.start.html#pandas.RangeIndex.start "pandas.RangeIndex.start")

The start value of the RangeIndex.

[`RangeIndex.step`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.step.html#pandas.RangeIndex.step "pandas.RangeIndex.step")

The step size between elements in the RangeIndex.

Examples

\>>> idx \= pd.RangeIndex(5)
\>>> idx.stop
5

Copy to clipboard

\>>> idx \= pd.RangeIndex(2, \-10, \-3)
\>>> idx.stop
\-10

Copy to clipboard

On this page