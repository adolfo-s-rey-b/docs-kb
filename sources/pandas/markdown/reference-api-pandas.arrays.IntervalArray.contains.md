[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.contains.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.contains.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.contains.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.contains.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.contains.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.contains.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.contains.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.contains.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.contains.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.contains.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.contains.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.contains.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.contains.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.contains.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.contains[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.contains.html#pandas-arrays-intervalarray-contains "Link to this heading")

============================================================================================================================================================================================

IntervalArray.contains(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L1828-L1867)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.contains.html#pandas.arrays.IntervalArray.contains "Link to this definition")

Check elementwise if the Intervals contain the value.

Return a boolean mask whether the value is contained in the Intervals of the IntervalArray.

Parameters:

**other**scalar

The value to check whether it is contained in the Intervals.

Returns:

boolean array

A boolean mask whether the value is contained in the Intervals.

See also

`Interval.contains`

Check whether Interval object contains value.

[`IntervalArray.overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.overlaps.html#pandas.arrays.IntervalArray.overlaps "pandas.arrays.IntervalArray.overlaps")

Check if an Interval overlaps the values in the IntervalArray.

Examples

\>>> intervals \= pd.arrays.IntervalArray.from\_tuples(\[(0, 1), (1, 3), (2, 4)\])
\>>> intervals
<IntervalArray>
\[(0, 1\], (1, 3\], (2, 4\]\]
Length: 3, dtype: interval\[int64, right\]

Copy to clipboard

\>>> intervals.contains(0.5)
array(\[ True, False, False\])

Copy to clipboard

On this page