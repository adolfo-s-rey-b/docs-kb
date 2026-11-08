[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_breaks.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.from\_breaks[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_breaks.html#pandas-arrays-intervalarray-from-breaks "Link to this heading")

======================================================================================================================================================================================================

classmethod IntervalArray.from\_breaks(_breaks_, _closed\='right'_, _copy\=False_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L400-L447)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_breaks.html#pandas.arrays.IntervalArray.from_breaks "Link to this definition")

Construct an IntervalArray from an array of splits.

This method creates intervals from consecutive pairs of break points, where each break point is the right edge of one interval and the left edge of the next.

Parameters:

**breaks**array-like (1-dimensional)

Left and right bounds for each interval.

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}, default ‘right’

Whether the intervals are closed on the left-side, right-side, both or neither.

**copy**bool, default False

Copy the data.

**dtype**dtype or None, default None

If None, dtype will be inferred.

Returns:

IntervalArray

See also

`interval_range`

Function to create a fixed frequency IntervalIndex.

[`IntervalArray.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_arrays.html#pandas.arrays.IntervalArray.from_arrays "pandas.arrays.IntervalArray.from_arrays")

Construct from a left and right array.

[`IntervalArray.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_tuples.html#pandas.arrays.IntervalArray.from_tuples "pandas.arrays.IntervalArray.from_tuples")

Construct from a sequence of tuples.

Examples

\>>> pd.arrays.IntervalArray.from\_breaks(\[0, 1, 2, 3\])
<IntervalArray>
\[(0, 1\], (1, 2\], (2, 3\]\]
Length: 3, dtype: interval\[int64, right\]

Copy to clipboard

On this page