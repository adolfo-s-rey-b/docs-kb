[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.mid.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.mid.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.mid.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.mid.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.mid.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.mid.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.mid.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.mid.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.mid.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.mid.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.mid.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.mid.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.mid.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.mid.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.mid[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.mid.html#pandas-arrays-intervalarray-mid "Link to this heading")

=============================================================================================================================================================================

property IntervalArray.mid[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L1330-L1360)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.mid.html#pandas.arrays.IntervalArray.mid "Link to this definition")

Return the midpoint of each Interval in the IntervalArray as an Index.

The midpoint of an interval is calculated as the average of its `left` and `right` bounds. This property returns a `pandas.Index` object containing the midpoint for each interval.

See also

`Interval.left`

Return left bound for the interval.

`Interval.right`

Return right bound for the interval.

`Interval.length`

Return the length of each interval.

Examples

\>>> interv\_arr \= pd.arrays.IntervalArray(\[pd.Interval(0, 1), pd.Interval(1, 5)\])
\>>> interv\_arr
<IntervalArray>
\[(0, 1\], (1, 5\]\]
Length: 2, dtype: interval\[int64, right\]
\>>> interv\_arr.mid
Index(\[0.5, 3.0\], dtype='float64')

Copy to clipboard

On this page