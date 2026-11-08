[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_arrays.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.from\_arrays[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_arrays.html#pandas-intervalindex-from-arrays "Link to this heading")

=================================================================================================================================================================================

classmethod IntervalIndex.from\_arrays(_left_, _right_, _closed\='right'_, _name\=None_, _copy\=False_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L668-L738)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_arrays.html#pandas.IntervalIndex.from_arrays "Link to this definition")

Construct from two arrays defining the left and right bounds.

Each interval is formed by pairing the corresponding elements of _left_ and _right_, producing an [`IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")
 of the same length as the input arrays.

Parameters:

**left**array-like (1-dimensional)

Left bounds for each interval.

**right**array-like (1-dimensional)

Right bounds for each interval.

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}, default ‘right’

Whether the intervals are closed on the left-side, right-side, both or neither.

**name**str, optional

Name of the resulting IntervalIndex.

**copy**bool, default False

Copy the data.

**dtype**dtype, optional

If None, dtype will be inferred.

Returns:

IntervalIndex

Raises:

ValueError

When a value is missing in only one of left or right. When a value in left is greater than the corresponding value in right.

See also

[`interval_range`](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas.interval_range "pandas.interval_range")

Function to create a fixed frequency IntervalIndex.

[`IntervalIndex.from_breaks`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_breaks.html#pandas.IntervalIndex.from_breaks "pandas.IntervalIndex.from_breaks")

Construct an IntervalIndex from an array of splits.

[`IntervalIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_tuples.html#pandas.IntervalIndex.from_tuples "pandas.IntervalIndex.from_tuples")

Construct an IntervalIndex from an array-like of tuples.

Notes

Each element of left must be less than or equal to the right element at the same position. If an element is missing, it must be missing in both left and right. A TypeError is raised when using an unsupported type for left or right. At the moment, ‘category’, ‘object’, and ‘string’ subtypes are not supported.

Examples

\>>> pd.IntervalIndex.from\_arrays(\[0, 1, 2\], \[1, 2, 3\])
IntervalIndex(\[(0, 1\], (1, 2\], (2, 3\]\],
              dtype='interval\[int64, right\]')

Copy to clipboard

On this page