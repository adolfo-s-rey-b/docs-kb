[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.closed.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.closed.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.closed.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.closed.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.closed.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.closed.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.closed.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.closed.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.closed.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.closed.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.closed.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.closed.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.closed.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.closed.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.closed[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.closed.html#pandas-arrays-intervalarray-closed "Link to this heading")

======================================================================================================================================================================================

property IntervalArray.closed[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L1434-L1468)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.closed.html#pandas.arrays.IntervalArray.closed "Link to this definition")

String describing the inclusive side the intervals.

Either `left`, `right`, `both` or `neither`.

See also

[`IntervalArray.closed`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.closed.html#pandas.arrays.IntervalArray.closed "pandas.arrays.IntervalArray.closed")

Returns inclusive side of the IntervalArray.

`Interval.closed`

Returns inclusive side of the Interval.

`IntervalIndex.closed`

Returns inclusive side of the IntervalIndex.

Examples

For arrays:

\>>> interv\_arr \= pd.arrays.IntervalArray(\[pd.Interval(0, 1), pd.Interval(1, 5)\])
\>>> interv\_arr
<IntervalArray>
\[(0, 1\], (1, 5\]\]
Length: 2, dtype: interval\[int64, right\]
\>>> interv\_arr.closed
'right'

Copy to clipboard

For Interval Index:

\>>> interv\_idx \= pd.interval\_range(start\=0, end\=2)
\>>> interv\_idx
IntervalIndex(\[(0, 1\], (1, 2\]\], dtype='interval\[int64, right\]')
\>>> interv\_idx.closed
'right'

Copy to clipboard

On this page