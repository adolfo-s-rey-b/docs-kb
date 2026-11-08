[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.contains.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.contains[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.contains.html#pandas-intervalindex-contains "Link to this heading")

=======================================================================================================================================================================

IntervalIndex.contains(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L553-L586)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.contains.html#pandas.IntervalIndex.contains "Link to this definition")

Check elementwise if the Intervals contain the value.

Return a boolean mask whether the value is contained in the Intervals of the IntervalIndex.

Parameters:

**other**scalar

The value to check whether it is contained in the Intervals.

Returns:

numpy.ndarray\[bool\]

A boolean mask whether the value is contained in the Intervals.

See also

`IntervalIndex.__contains__`

Check whether an Interval is one of the IntervalIndex’s elements.

[`IntervalIndex.overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.overlaps.html#pandas.IntervalIndex.overlaps "pandas.IntervalIndex.overlaps")

Check if an Interval overlaps the values in the IntervalIndex.

Examples

\>>> intervals \= pd.IntervalIndex.from\_tuples(\[(0, 1), (1, 3), (2, 4)\])
\>>> intervals
IntervalIndex(\[(0, 1\], (1, 3\], (2, 4\]\], dtype='interval\[int64, right\]')

Copy to clipboard

\>>> intervals.contains(0.5)
array(\[ True, False, False\])

Copy to clipboard

On this page