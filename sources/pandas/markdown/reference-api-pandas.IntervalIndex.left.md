[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.left.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.left.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.left.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.left.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.left.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.left.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.left.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.left.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.left.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.left.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.left.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.left.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.left.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.left.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.left[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.left.html#pandas-intervalindex-left "Link to this heading")

===========================================================================================================================================================

IntervalIndex.left[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L1415-L1450)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.left.html#pandas.IntervalIndex.left "Link to this definition")

Return left bounds of the intervals in the IntervalIndex.

The left bounds of each interval in the IntervalIndex are returned as an Index. The datatype of the left bounds is the same as the datatype of the endpoints of the intervals.

Returns:

Index

An Index containing the left bounds of the intervals.

See also

[`IntervalIndex.right`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.right.html#pandas.IntervalIndex.right "pandas.IntervalIndex.right")

Return the right bounds of the intervals in the IntervalIndex.

[`IntervalIndex.mid`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.mid.html#pandas.IntervalIndex.mid "pandas.IntervalIndex.mid")

Return the mid-point of the intervals in the IntervalIndex.

[`IntervalIndex.length`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.length.html#pandas.IntervalIndex.length "pandas.IntervalIndex.length")

Return the length of the intervals in the IntervalIndex.

Examples

\>>> iv\_idx \= pd.IntervalIndex.from\_arrays(\[1, 2, 3\], \[4, 5, 6\], closed\="right")
\>>> iv\_idx.left
Index(\[1, 2, 3\], dtype='int64')

Copy to clipboard

\>>> iv\_idx \= pd.IntervalIndex.from\_tuples(
...     \[(1, 4), (2, 5), (3, 6)\], closed\="left"
... )
\>>> iv\_idx.left
Index(\[1, 2, 3\], dtype='int64')

Copy to clipboard

On this page