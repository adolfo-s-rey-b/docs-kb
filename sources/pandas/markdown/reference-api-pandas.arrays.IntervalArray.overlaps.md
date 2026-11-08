[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.overlaps.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.overlaps.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.overlaps.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.overlaps[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.overlaps.html#pandas-arrays-intervalarray-overlaps "Link to this heading")

============================================================================================================================================================================================

IntervalArray.overlaps(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L1362-L1430)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.overlaps.html#pandas.arrays.IntervalArray.overlaps "Link to this definition")

Check elementwise if an Interval overlaps the values in the IntervalArray.

Two intervals overlap if they share a common point, including closed endpoints. Intervals that only have an open endpoint in common do not overlap, and empty intervals contain no points at all, so they never overlap.

Parameters:

**other**IntervalArray

Interval to check against for an overlap.

Returns:

ndarray

Boolean array positionally indicating where an overlap occurs.

See also

`Interval.overlaps`

Check whether two Interval objects overlap.

Examples

\>>> data \= \[(0, 1), (1, 3), (2, 4)\]
\>>> intervals \= pd.arrays.IntervalArray.from\_tuples(data)
\>>> intervals
<IntervalArray>
\[(0, 1\], (1, 3\], (2, 4\]\]
Length: 3, dtype: interval\[int64, right\]

Copy to clipboard

\>>> intervals.overlaps(pd.Interval(0.5, 1.5))
array(\[ True,  True, False\])

Copy to clipboard

Intervals that share closed endpoints overlap:

\>>> intervals.overlaps(pd.Interval(1, 3, closed\="left"))
array(\[ True,  True, True\])

Copy to clipboard

Intervals that only have an open endpoint in common do not overlap:

\>>> intervals.overlaps(pd.Interval(1, 2, closed\="right"))
array(\[False,  True, False\])

Copy to clipboard

Empty intervals do not overlap with anything:

\>>> intervals.overlaps(pd.Interval(1, 1, closed\="left"))
array(\[False, False, False\])

Copy to clipboard

On this page