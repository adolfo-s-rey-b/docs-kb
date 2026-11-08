[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.right.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.right.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.right.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.right.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.right.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.right.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.right.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.right.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.right.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.right.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.right.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.right.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.right.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.right.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.right[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.right.html#pandas-arrays-intervalarray-right "Link to this heading")

===================================================================================================================================================================================

property IntervalArray.right[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L1263-L1296)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.right.html#pandas.arrays.IntervalArray.right "Link to this definition")

Return the right endpoints of each Interval in the IntervalArray as an Index.

This property extracts the right endpoints from each interval contained within the IntervalArray. This can be helpful in use cases where you need to work with or compare only the upper bounds of intervals, such as when performing range-based filtering, determining interval overlaps, or visualizing the end boundaries of data segments.

See also

`arrays.IntervalArray.left`

Return the left endpoints of each Interval in the IntervalArray as an Index.

`arrays.IntervalArray.mid`

Return the midpoint of each Interval in the IntervalArray as an Index.

`arrays.IntervalArray.contains`

Check elementwise if the Intervals contain the value.

Examples

\>>> interv\_arr \= pd.arrays.IntervalArray(\[pd.Interval(0, 1), pd.Interval(2, 5)\])
\>>> interv\_arr
<IntervalArray>
\[(0, 1\], (2, 5\]\]
Length: 2, dtype: interval\[int64, right\]
\>>> interv\_arr.right
Index(\[1, 5\], dtype='int64')

Copy to clipboard

On this page