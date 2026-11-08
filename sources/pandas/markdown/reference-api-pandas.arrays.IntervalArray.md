[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas-arrays-intervalarray "Link to this heading")

=================================================================================================================================================================

class pandas.arrays.IntervalArray(_data_, _closed\=None_, _dtype\=None_, _copy\=False_, _verify\_integrity\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L123-L1932)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "Link to this definition")

Pandas array for interval data that are closed on the same side.

An IntervalArray stores an array of Interval objects, where each Interval represents a contiguous span of values. All intervals in the array must have the same closure (left, right, both, or neither).

Parameters:

**data**array-like (1-dimensional)

Array-like (ndarray, [`DatetimeArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray "pandas.arrays.DatetimeArray")
, [`TimedeltaArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html#pandas.arrays.TimedeltaArray "pandas.arrays.TimedeltaArray")
) containing Interval objects from which to build the IntervalArray.

**closed**{‘left’, ‘right’, ‘both’, ‘neither’}, default ‘right’

Whether the intervals are closed on the left-side, right-side, both or neither.

**dtype**dtype or None, default None

If None, dtype will be inferred.

**copy**bool, default False

Copy the input data.

**verify\_integrity**bool, default True

Verify that the IntervalArray is valid.

Attributes

|     |     |
| --- | --- |
| [`left`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.left.html#pandas.arrays.IntervalArray.left "pandas.arrays.IntervalArray.left") | Return the left endpoints of each Interval in the IntervalArray as an Index. |
| [`right`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.right.html#pandas.arrays.IntervalArray.right "pandas.arrays.IntervalArray.right") | Return the right endpoints of each Interval in the IntervalArray as an Index. |
| [`closed`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.closed.html#pandas.arrays.IntervalArray.closed "pandas.arrays.IntervalArray.closed") | String describing the inclusive side the intervals. |
| [`mid`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.mid.html#pandas.arrays.IntervalArray.mid "pandas.arrays.IntervalArray.mid") | Return the midpoint of each Interval in the IntervalArray as an Index. |
| [`length`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.length.html#pandas.arrays.IntervalArray.length "pandas.arrays.IntervalArray.length") | Return an Index with entries denoting the length of each Interval. |
| [`is_empty`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.is_empty.html#pandas.arrays.IntervalArray.is_empty "pandas.arrays.IntervalArray.is_empty") | Indicates if an interval is empty, meaning it contains no points. |
| [`is_non_overlapping_monotonic`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.is_non_overlapping_monotonic.html#pandas.arrays.IntervalArray.is_non_overlapping_monotonic "pandas.arrays.IntervalArray.is_non_overlapping_monotonic") | Return a boolean whether the IntervalArray/IntervalIndex is non-overlapping and monotonic. |

Methods

|     |     |
| --- | --- |
| [`from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_arrays.html#pandas.arrays.IntervalArray.from_arrays "pandas.arrays.IntervalArray.from_arrays")<br>(left, right\[, closed, copy, dtype\]) | Construct from two arrays defining the left and right bounds. |
| [`from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_tuples.html#pandas.arrays.IntervalArray.from_tuples "pandas.arrays.IntervalArray.from_tuples")<br>(data\[, closed, copy, dtype\]) | Construct an IntervalArray from an array-like of tuples. |
| [`from_breaks`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_breaks.html#pandas.arrays.IntervalArray.from_breaks "pandas.arrays.IntervalArray.from_breaks")<br>(breaks\[, closed, copy, dtype\]) | Construct an IntervalArray from an array of splits. |
| [`contains`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.contains.html#pandas.arrays.IntervalArray.contains "pandas.arrays.IntervalArray.contains")<br>(other) | Check elementwise if the Intervals contain the value. |
| [`overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.overlaps.html#pandas.arrays.IntervalArray.overlaps "pandas.arrays.IntervalArray.overlaps")<br>(other) | Check elementwise if an Interval overlaps the values in the IntervalArray. |
| [`set_closed`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.set_closed.html#pandas.arrays.IntervalArray.set_closed "pandas.arrays.IntervalArray.set_closed")<br>(closed) | Return an identical IntervalArray closed on the specified side. |
| [`to_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.to_tuples.html#pandas.arrays.IntervalArray.to_tuples "pandas.arrays.IntervalArray.to_tuples")<br>(\[na\_tuple\]) | Return an ndarray (if self is IntervalArray) or Index (if self is IntervalIndex) of tuples of the form (left, right). |

See also

`Index`

The base pandas Index type.

`Interval`

A bounded slice-like interval; the elements of an IntervalArray.

`interval_range`

Function to create a fixed frequency IntervalIndex.

`cut`

Bin values into discrete Intervals.

`qcut`

Bin values into equal-sized Intervals based on rank or sample quantiles.

Notes

See the [user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#intervalindex)
 for more.

Examples

A new `IntervalArray` can be constructed directly from an array-like of `Interval` objects: >>> pd.arrays.IntervalArray(\[pd.Interval(0, 1), pd.Interval(1, 5)\]) <IntervalArray> \[(0, 1\], (1, 5\]\] Length: 2, dtype: interval\[int64, right\]

It may also be constructed using one of the constructor methods: [`IntervalArray.from_arrays()`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_arrays.html#pandas.arrays.IntervalArray.from_arrays "pandas.arrays.IntervalArray.from_arrays")
, [`IntervalArray.from_breaks()`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_breaks.html#pandas.arrays.IntervalArray.from_breaks "pandas.arrays.IntervalArray.from_breaks")
, and [`IntervalArray.from_tuples()`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.from_tuples.html#pandas.arrays.IntervalArray.from_tuples "pandas.arrays.IntervalArray.from_tuples")
.

On this page