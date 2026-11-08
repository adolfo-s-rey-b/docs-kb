[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.length.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.length.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.length.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.length.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.length.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.length.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.length.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.length.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.length.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.length.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.length.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.length.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.length.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.length.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.length[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.length.html#pandas-arrays-intervalarray-length "Link to this heading")

======================================================================================================================================================================================

property IntervalArray.length[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L1298-L1328)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.length.html#pandas.arrays.IntervalArray.length "Link to this definition")

Return an Index with entries denoting the length of each Interval.

The length of an interval is calculated as the difference between its right and left bounds. This property is particularly useful when working with intervals where the size of the interval is an important attribute, such as in time-series analysis or spatial data analysis.

See also

`arrays.IntervalArray.left`

Return the left endpoints of each Interval in the IntervalArray as an Index.

`arrays.IntervalArray.right`

Return the right endpoints of each Interval in the IntervalArray as an Index.

`arrays.IntervalArray.mid`

Return the midpoint of each Interval in the IntervalArray as an Index.

Examples

\>>> interv\_arr \= pd.arrays.IntervalArray(\[pd.Interval(0, 1), pd.Interval(1, 5)\])
\>>> interv\_arr
<IntervalArray>
\[(0, 1\], (1, 5\]\]
Length: 2, dtype: interval\[int64, right\]
\>>> interv\_arr.length
Index(\[1, 4\], dtype='int64')

Copy to clipboard

On this page