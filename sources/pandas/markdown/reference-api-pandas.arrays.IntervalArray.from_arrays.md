[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_arrays.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.from_arrays.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.from_arrays.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.from\_arrays[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_arrays.html#pandas-arrays-intervalarray-from-arrays "Link to this heading")

======================================================================================================================================================================================================

classmethod IntervalArray.from\_arrays(_left_, _right_, _closed\='right'_, _copy\=False_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L449-L524)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_arrays.html#pandas.arrays.IntervalArray.from_arrays "Link to this definition")

Construct from two arrays defining the left and right bounds.

This method creates an IntervalArray from two arrays of equal length, where the i-th interval spans from left\[i\] to right\[i\].

Parameters:

**left**array-like (1-dimensional)

Left bounds for each interval.

**right**array-like (1-dimensional)

Right bounds for each interval.

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}, default ‘right’

Whether the intervals are closed on the left-side, right-side, both or neither.

**copy**bool, default False

Copy the data.

**dtype**dtype, optional

If None, dtype will be inferred.

Returns:

IntervalArray

Raises:

ValueError

When a value is missing in only one of left or right. When a value in left is greater than the corresponding value in right.

See also

`interval_range`

Function to create a fixed frequency IntervalIndex.

[`IntervalArray.from_breaks`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_breaks.html#pandas.arrays.IntervalArray.from_breaks "pandas.arrays.IntervalArray.from_breaks")

Construct an IntervalArray from an array of splits.

[`IntervalArray.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_tuples.html#pandas.arrays.IntervalArray.from_tuples "pandas.arrays.IntervalArray.from_tuples")

Construct an IntervalArray from an array-like of tuples.

Notes

Each element of left must be less than or equal to the right element at the same position. If an element is missing, it must be missing in both left and right. A TypeError is raised when using an unsupported type for left or right. At the moment, ‘category’, ‘object’, and ‘string’ subtypes are not supported.

Examples

\>>> pd.arrays.IntervalArray.from\_arrays(\[0, 1, 2\], \[1, 2, 3\])
<IntervalArray>
\[(0, 1\], (1, 2\], (2, 3\]\]
Length: 3, dtype: interval\[int64, right\]

Copy to clipboard

On this page