[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_tuples.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.from_tuples.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.from_tuples.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.from\_tuples[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_tuples.html#pandas-arrays-intervalarray-from-tuples "Link to this heading")

======================================================================================================================================================================================================

classmethod IntervalArray.from\_tuples(_data_, _closed\='right'_, _copy\=False_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L526-L594)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_tuples.html#pandas.arrays.IntervalArray.from_tuples "Link to this definition")

Construct an IntervalArray from an array-like of tuples.

This method creates an IntervalArray from a sequence of (left, right) tuples, where each tuple defines the bounds of an interval.

Parameters:

**data**array-like (1-dimensional)

Array of tuples.

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}, default ‘right’

Whether the intervals are closed on the left-side, right-side, both or neither.

**copy**bool, default False

By-default copy the data, this is compat only and ignored.

**dtype**dtype or None, default None

If None, dtype will be inferred.

Returns:

IntervalArray

See also

`interval_range`

Function to create a fixed frequency IntervalIndex.

[`IntervalArray.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_arrays.html#pandas.arrays.IntervalArray.from_arrays "pandas.arrays.IntervalArray.from_arrays")

Construct an IntervalArray from a left and right array.

[`IntervalArray.from_breaks`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_breaks.html#pandas.arrays.IntervalArray.from_breaks "pandas.arrays.IntervalArray.from_breaks")

Construct an IntervalArray from an array of splits.

Examples

\>>> pd.arrays.IntervalArray.from\_tuples(\[(0, 1), (1, 2)\])
<IntervalArray>
\[(0, 1\], (1, 2\]\]
Length: 2, dtype: interval\[int64, right\]

Copy to clipboard

On this page