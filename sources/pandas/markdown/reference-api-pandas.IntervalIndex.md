[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas-intervalindex "Link to this heading")

============================================================================================================================================

class pandas.IntervalIndex(_data_, _closed\=None_, _dtype\=None_, _copy\=None_, _name\=None_, _verify\_integrity\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L145-L1650)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "Link to this definition")

Immutable index of intervals that are closed on the same side.

An `IntervalIndex` stores an array of [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
 objects, all sharing the same `closed` value, enabling vectorized operations such as overlap checks, containment tests, and set-like comparisons on intervals. It is commonly produced by [`cut()`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")
, [`qcut()`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#pandas.qcut "pandas.qcut")
, or [`interval_range()`](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas.interval_range "pandas.interval_range")
.

Parameters:

**data**array-like (1-dimensional)

Array-like (ndarray, `DateTimeArray`, `TimeDeltaArray`) containing Interval objects from which to build the IntervalIndex.

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}, default ‘right’

Whether the intervals are closed on the left-side, right-side, both or neither.

**dtype**dtype or None, default None

If None, dtype will be inferred.

**copy**bool, default None

Whether to copy input data, only relevant for array, Series, and Index inputs (for other input, e.g. a list, a new array is created anyway). Defaults to True for array input and False for Index/Series. Set to False to avoid copying array input at your own risk (if you know the input data won’t be modified elsewhere). Set to True to force copying Series/Index input up front.

**name**object, optional

Name to be stored in the index.

**verify\_integrity**bool, default True

Verify that the IntervalIndex is valid.

Attributes

|     |     |
| --- | --- |
| [`left`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.left.html#pandas.IntervalIndex.left "pandas.IntervalIndex.left") | Return left bounds of the intervals in the IntervalIndex. |
| [`right`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.right.html#pandas.IntervalIndex.right "pandas.IntervalIndex.right") | Return right bounds of the intervals in the IntervalIndex. |
| [`closed`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed.html#pandas.IntervalIndex.closed "pandas.IntervalIndex.closed") | String describing the inclusive side of the intervals. |
| [`mid`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.mid.html#pandas.IntervalIndex.mid "pandas.IntervalIndex.mid") | Return the midpoint of each interval in the IntervalIndex as an Index. |
| [`length`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.length.html#pandas.IntervalIndex.length "pandas.IntervalIndex.length") | Calculate the length of each interval in the IntervalIndex. |
| [`is_empty`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_empty.html#pandas.IntervalIndex.is_empty "pandas.IntervalIndex.is_empty") | Indicates if an interval is empty, meaning it contains no points. |
| [`is_non_overlapping_monotonic`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_non_overlapping_monotonic.html#pandas.IntervalIndex.is_non_overlapping_monotonic "pandas.IntervalIndex.is_non_overlapping_monotonic") | Return True if the IntervalIndex is non-overlapping and monotonic. |
| [`is_overlapping`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_overlapping.html#pandas.IntervalIndex.is_overlapping "pandas.IntervalIndex.is_overlapping") | Return True if the IntervalIndex has overlapping intervals, else False. |
| [`values`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.values.html#pandas.IntervalIndex.values "pandas.IntervalIndex.values") | Return an array representing the data in the Index. |

Methods

|     |     |
| --- | --- |
| [`from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_arrays.html#pandas.IntervalIndex.from_arrays "pandas.IntervalIndex.from_arrays")<br>(left, right\[, closed, name, ...\]) | Construct from two arrays defining the left and right bounds. |
| [`from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_tuples.html#pandas.IntervalIndex.from_tuples "pandas.IntervalIndex.from_tuples")<br>(data\[, closed, name, copy, dtype\]) | Construct an IntervalIndex from an array-like of tuples. |
| [`from_breaks`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_breaks.html#pandas.IntervalIndex.from_breaks "pandas.IntervalIndex.from_breaks")<br>(breaks\[, closed, name, copy, dtype\]) | Construct an IntervalIndex from an array of splits. |
| [`get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.get_loc.html#pandas.IntervalIndex.get_loc "pandas.IntervalIndex.get_loc")<br>(key) | Get integer location, slice or boolean mask for requested label. |
| [`get_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.get_indexer.html#pandas.IntervalIndex.get_indexer "pandas.IntervalIndex.get_indexer")<br>(target\[, method, limit, tolerance\]) | Compute indexer and mask for new index given the current index. |
| [`contains`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.contains.html#pandas.IntervalIndex.contains "pandas.IntervalIndex.contains")<br>(other) | Check elementwise if the Intervals contain the value. |
| [`overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.overlaps.html#pandas.IntervalIndex.overlaps "pandas.IntervalIndex.overlaps")<br>(other) | Check elementwise if an Interval overlaps the values in the IntervalIndex. |
| [`set_closed`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.set_closed.html#pandas.IntervalIndex.set_closed "pandas.IntervalIndex.set_closed")<br>(closed) | Return an identical IntervalIndex closed on the specified side. |
| [`to_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.to_tuples.html#pandas.IntervalIndex.to_tuples "pandas.IntervalIndex.to_tuples")<br>(\[na\_tuple\]) | Return an Index of tuples of the form (left, right). |

See also

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

The base pandas Index type.

[`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")

A bounded slice-like interval; the elements of an IntervalIndex.

[`interval_range`](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas.interval_range "pandas.interval_range")

Function to create a fixed frequency IntervalIndex.

[`cut`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")

Bin values into discrete Intervals.

[`qcut`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#pandas.qcut "pandas.qcut")

Bin values into equal-sized Intervals based on rank or sample quantiles.

Notes

See the [user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#intervalindex)
 for more.

Examples

A new `IntervalIndex` is typically constructed using [`interval_range()`](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas.interval_range "pandas.interval_range")
:

\>>> pd.interval\_range(start\=0, end\=5)
IntervalIndex(\[(0, 1\], (1, 2\], (2, 3\], (3, 4\], (4, 5\]\],
              dtype='interval\[int64, right\]')

Copy to clipboard

It may also be constructed using one of the constructor methods: [`IntervalIndex.from_arrays()`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_arrays.html#pandas.IntervalIndex.from_arrays "pandas.IntervalIndex.from_arrays")
, [`IntervalIndex.from_breaks()`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_breaks.html#pandas.IntervalIndex.from_breaks "pandas.IntervalIndex.from_breaks")
, and [`IntervalIndex.from_tuples()`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_tuples.html#pandas.IntervalIndex.from_tuples "pandas.IntervalIndex.from_tuples")
.

See further examples in the doc strings of `interval_range` and the mentioned constructor methods.

On this page