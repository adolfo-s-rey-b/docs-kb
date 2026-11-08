[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.to_tuples.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.IntervalArray.to_tuples.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.IntervalArray.to_tuples.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.IntervalArray.to\_tuples[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.to_tuples.html#pandas-arrays-intervalarray-to-tuples "Link to this heading")

================================================================================================================================================================================================

IntervalArray.to\_tuples(_na\_tuple\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/interval.py#L1671-L1724)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.to_tuples.html#pandas.arrays.IntervalArray.to_tuples "Link to this definition")

Return an ndarray (if self is IntervalArray) or Index (if self is IntervalIndex) of tuples of the form (left, right).

This method extracts the bounds of each interval as a tuple, useful for iteration or conversion to other data structures.

Parameters:

**na\_tuple**bool, default True

If `True`, return `NA` as a tuple `(nan, nan)`. If `False`, just return `NA` as `nan`.

Returns:

ndarray or Index

An ndarray of tuples representing the intervals

if self is an IntervalArray.

An Index of tuples representing the intervals

if self is an IntervalIndex.

See also

`IntervalArray.to_list`

Convert IntervalArray to a list of tuples.

`IntervalArray.to_numpy`

Convert IntervalArray to a numpy array.

`IntervalArray.unique`

Find unique intervals in an IntervalArray.

Examples

For `pandas.IntervalArray`:

\>>> idx \= pd.arrays.IntervalArray.from\_tuples(\[(0, 1), (1, 2)\])
\>>> idx
<IntervalArray>
\[(0, 1\], (1, 2\]\]
Length: 2, dtype: interval\[int64, right\]
\>>> idx.to\_tuples()
array(\[(np.int64(0), np.int64(1)), (np.int64(1), np.int64(2))\],
      dtype=object)

Copy to clipboard

For [`pandas.IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")
:

\>>> idx \= pd.interval\_range(start\=0, end\=2)
\>>> idx
IntervalIndex(\[(0, 1\], (1, 2\]\], dtype='interval\[int64, right\]')
\>>> idx.to\_tuples()
Index(\[(0, 1), (1, 2)\], dtype='object')

Copy to clipboard

On this page