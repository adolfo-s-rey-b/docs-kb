[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.mid.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.mid.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.mid.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.mid.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.mid.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.mid.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.mid.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.mid.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.mid.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.mid.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.mid.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.mid.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.mid.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.mid.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.mid[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.mid.html#pandas-intervalindex-mid "Link to this heading")

========================================================================================================================================================

IntervalIndex.mid[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L1489-L1528)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.mid.html#pandas.IntervalIndex.mid "Link to this definition")

Return the midpoint of each interval in the IntervalIndex as an Index.

Each midpoint is calculated as the average of the left and right bounds of each interval. The midpoints are returned as a pandas Index object.

Returns:

pandas.Index

An Index containing the midpoints of each interval.

See also

[`IntervalIndex.left`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.left.html#pandas.IntervalIndex.left "pandas.IntervalIndex.left")

Return the left bounds of the intervals in the IntervalIndex.

[`IntervalIndex.right`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.right.html#pandas.IntervalIndex.right "pandas.IntervalIndex.right")

Return the right bounds of the intervals in the IntervalIndex.

[`IntervalIndex.length`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.length.html#pandas.IntervalIndex.length "pandas.IntervalIndex.length")

Return the length of the intervals in the IntervalIndex.

Notes

The midpoint is the average of the interval bounds, potentially resulting in a floating-point number even if bounds are integers. The returned Index will have a dtype that accurately holds the midpoints. This computation is the same regardless of whether intervals are open or closed.

Examples

\>>> iv\_idx \= pd.IntervalIndex.from\_arrays(\[1, 2, 3\], \[4, 5, 6\])
\>>> iv\_idx.mid
Index(\[2.5, 3.5, 4.5\], dtype='float64')

Copy to clipboard

\>>> iv\_idx \= pd.IntervalIndex.from\_tuples(\[(1, 4), (2, 5), (3, 6)\])
\>>> iv\_idx.mid
Index(\[2.5, 3.5, 4.5\], dtype='float64')

Copy to clipboard

On this page