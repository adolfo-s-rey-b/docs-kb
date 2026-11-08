[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.start.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.RangeIndex.start[#](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.start.html#pandas-rangeindex-start "Link to this heading")

=====================================================================================================================================================

property RangeIndex.start[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/range.py#L335-L361)
[#](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.start.html#pandas.RangeIndex.start "Link to this definition")

The value of the start parameter (`0` if this was not supplied).

This property returns the starting value of the RangeIndex. If the start value is not explicitly provided during the creation of the RangeIndex, it defaults to 0.

See also

[`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")

Immutable index implementing a range-based index.

[`RangeIndex.stop`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.stop.html#pandas.RangeIndex.stop "pandas.RangeIndex.stop")

Returns the stop value of the RangeIndex.

[`RangeIndex.step`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.step.html#pandas.RangeIndex.step "pandas.RangeIndex.step")

Returns the step value of the RangeIndex.

Examples

\>>> idx \= pd.RangeIndex(5)
\>>> idx.start
0

Copy to clipboard

\>>> idx \= pd.RangeIndex(2, \-10, \-3)
\>>> idx.start
2

Copy to clipboard

On this page