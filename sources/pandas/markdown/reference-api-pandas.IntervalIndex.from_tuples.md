[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_tuples.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.from\_tuples[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_tuples.html#pandas-intervalindex-from-tuples "Link to this heading")

=================================================================================================================================================================================

classmethod IntervalIndex.from\_tuples(_data_, _closed\='right'_, _name\=None_, _copy\=False_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L740-L789)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_tuples.html#pandas.IntervalIndex.from_tuples "Link to this definition")

Construct an IntervalIndex from an array-like of tuples.

Each tuple in _data_ should contain exactly two elements representing the left and right bounds of an interval.

Parameters:

**data**array-like (1-dimensional)

Array of tuples.

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}, default ‘right’

Whether the intervals are closed on the left-side, right-side, both or neither.

**name**str, optional

Name of the resulting IntervalIndex.

**copy**bool, default False

By-default copy the data, this is compat only and ignored.

**dtype**dtype or None, default None

If None, dtype will be inferred.

Returns:

IntervalIndex

See also

[`interval_range`](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas.interval_range "pandas.interval_range")

Function to create a fixed frequency IntervalIndex.

[`IntervalIndex.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_arrays.html#pandas.IntervalIndex.from_arrays "pandas.IntervalIndex.from_arrays")

Construct an IntervalIndex from a left and right array.

[`IntervalIndex.from_breaks`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_breaks.html#pandas.IntervalIndex.from_breaks "pandas.IntervalIndex.from_breaks")

Construct an IntervalIndex from an array of splits.

Examples

\>>> pd.IntervalIndex.from\_tuples(\[(0, 1), (1, 2)\])
IntervalIndex(\[(0, 1\], (1, 2\]\],
               dtype='interval\[int64, right\]')

Copy to clipboard

On this page