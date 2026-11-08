[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.step.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.RangeIndex.step[#](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.step.html#pandas-rangeindex-step "Link to this heading")

==================================================================================================================================================

property RangeIndex.step[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/range.py#L391-L423)
[#](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.step.html#pandas.RangeIndex.step "Link to this definition")

The value of the step parameter (`1` if this was not supplied).

The `step` parameter determines the increment (or decrement in the case of negative values) between consecutive elements in the `RangeIndex`.

See also

[`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")

Immutable index implementing a range-based index.

[`RangeIndex.stop`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.stop.html#pandas.RangeIndex.stop "pandas.RangeIndex.stop")

Returns the stop value of the RangeIndex.

[`RangeIndex.start`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.start.html#pandas.RangeIndex.start "pandas.RangeIndex.start")

Returns the start value of the RangeIndex.

Examples

\>>> idx \= pd.RangeIndex(5)
\>>> idx.step
1

Copy to clipboard

\>>> idx \= pd.RangeIndex(2, \-10, \-3)
\>>> idx.step
\-3

Copy to clipboard

Even if [`pandas.RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")
 is empty, `step` is still `1` if not supplied.

\>>> idx \= pd.RangeIndex(1, 0)
\>>> idx.step
1

Copy to clipboard

On this page