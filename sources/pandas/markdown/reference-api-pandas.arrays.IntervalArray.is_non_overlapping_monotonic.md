[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.is\_non\_overlapping\_monotonic[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html#pandas-arrays-intervalarray-is-non-overlapping-monotonic "Link to this heading")

===========================================================================================================================================================================================================================================================

property IntervalArray.is\_non\_overlapping\_monotonic[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L1513-L1579)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html#pandas.arrays.IntervalArray.is_non_overlapping_monotonic "Link to this definition")

Return a boolean whether the IntervalArray/IntervalIndex is non-overlapping and monotonic.

Non-overlapping means (no Intervals share points), and monotonic means either monotonic increasing or monotonic decreasing.

See also

[`overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.overlaps.html#pandas.arrays.IntervalArray.overlaps "pandas.arrays.IntervalArray.overlaps")

Check if two IntervalIndex objects overlap.

Examples

For arrays:

\>>> interv\_arr \= pd.arrays.IntervalArray(\[pd.Interval(0, 1), pd.Interval(1, 5)\])
\>>> interv\_arr
<IntervalArray>
\[(0, 1\], (1, 5\]\]
Length: 2, dtype: interval\[int64, right\]
\>>> interv\_arr.is\_non\_overlapping\_monotonic
True

Copy to clipboard

\>>> interv\_arr \= pd.arrays.IntervalArray(
...     \[pd.Interval(0, 1), pd.Interval(\-1, 0.1)\]
... )
\>>> interv\_arr
<IntervalArray>
\[(0.0, 1.0\], (-1.0, 0.1\]\]
Length: 2, dtype: interval\[float64, right\]
\>>> interv\_arr.is\_non\_overlapping\_monotonic
False

Copy to clipboard

For Interval Index:

\>>> interv\_idx \= pd.interval\_range(start\=0, end\=2)
\>>> interv\_idx
IntervalIndex(\[(0, 1\], (1, 2\]\], dtype='interval\[int64, right\]')
\>>> interv\_idx.is\_non\_overlapping\_monotonic
True

Copy to clipboard

\>>> interv\_idx \= pd.interval\_range(start\=0, end\=2, closed\="both")
\>>> interv\_idx
IntervalIndex(\[\[0, 1\], \[1, 2\]\], dtype='interval\[int64, both\]')
\>>> interv\_idx.is\_non\_overlapping\_monotonic
False

Copy to clipboard

On this page