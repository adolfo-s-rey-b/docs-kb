[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.set_closed.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.set\_closed[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.set_closed.html#pandas-arrays-intervalarray-set-closed "Link to this heading")

===================================================================================================================================================================================================

IntervalArray.set\_closed(_closed_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L1470-L1511)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.set_closed.html#pandas.arrays.IntervalArray.set_closed "Link to this definition")

Return an identical IntervalArray closed on the specified side.

This method creates a new IntervalArray with the same bounds but with a different closure specification.

Parameters:

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}

Whether the intervals are closed on the left-side, right-side, both or neither.

Returns:

IntervalArray

A new IntervalArray with the specified side closures.

See also

[`IntervalArray.closed`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.closed.html#pandas.arrays.IntervalArray.closed "pandas.arrays.IntervalArray.closed")

Returns inclusive side of the Interval.

`arrays.IntervalArray.closed`

Returns inclusive side of the IntervalArray.

Examples

\>>> index \= pd.arrays.IntervalArray.from\_breaks(range(4))
\>>> index
<IntervalArray>
\[(0, 1\], (1, 2\], (2, 3\]\]
Length: 3, dtype: interval\[int64, right\]
\>>> index.set\_closed("both")
<IntervalArray>
\[\[0, 1\], \[1, 2\], \[2, 3\]\]
Length: 3, dtype: interval\[int64, both\]

Copy to clipboard

On this page