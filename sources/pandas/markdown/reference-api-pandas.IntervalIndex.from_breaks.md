[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_breaks.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.from_breaks.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_breaks.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.from_breaks.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.from_breaks.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.from_breaks.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.from_breaks.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.from_breaks.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.from_breaks.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.from_breaks.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.from_breaks.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.from_breaks.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.from_breaks.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.from_breaks.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.from\_breaks[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_breaks.html#pandas-intervalindex-from-breaks "Link to this heading")

=================================================================================================================================================================================

classmethod IntervalIndex.from\_breaks(_breaks_, _closed\='right'_, _name\=None_, _copy\=False_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L616-L666)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_breaks.html#pandas.IntervalIndex.from_breaks "Link to this definition")

Construct an IntervalIndex from an array of splits.

The _breaks_ array of length _N_ is converted into _N-1_ adjacent, non-overlapping intervals whose endpoints are consecutive pairs of break values.

Parameters:

**breaks**array-like (1-dimensional)

Left and right bounds for each interval.

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}, default ‘right’

Whether the intervals are closed on the left-side, right-side, both or neither.

**name**str, optional

Name of the resulting IntervalIndex.

**copy**bool, default False

Copy the data.

**dtype**dtype or None, default None

If None, dtype will be inferred.

Returns:

IntervalIndex

See also

[`interval_range`](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas.interval_range "pandas.interval_range")

Function to create a fixed frequency IntervalIndex.

[`IntervalIndex.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_arrays.html#pandas.IntervalIndex.from_arrays "pandas.IntervalIndex.from_arrays")

Construct from a left and right array.

[`IntervalIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_tuples.html#pandas.IntervalIndex.from_tuples "pandas.IntervalIndex.from_tuples")

Construct from a sequence of tuples.

Examples

\>>> pd.IntervalIndex.from\_breaks(\[0, 1, 2, 3\])
IntervalIndex(\[(0, 1\], (1, 2\], (2, 3\]\],
              dtype='interval\[int64, right\]')

Copy to clipboard

On this page