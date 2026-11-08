[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.to_tuples.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.to_tuples.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.to_tuples.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.to_tuples.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.to_tuples.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.to_tuples.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.to_tuples.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.to_tuples.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.to_tuples.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.to_tuples.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.to_tuples.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.to_tuples.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.to_tuples.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.to_tuples.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.to\_tuples[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.to_tuples.html#pandas-intervalindex-to-tuples "Link to this heading")

===========================================================================================================================================================================

IntervalIndex.to\_tuples(_na\_tuple\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L475-L506)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.to_tuples.html#pandas.IntervalIndex.to_tuples "Link to this definition")

Return an Index of tuples of the form (left, right).

This method extracts the bounds of each interval as a tuple, useful for iteration or conversion to other data structures.

Parameters:

**na\_tuple**bool, default True

If `True`, return `NA` as a tuple `(nan, nan)`. If `False`, just return `NA` as `nan`.

Returns:

Index

An Index of tuples representing the intervals.

See also

[`arrays.IntervalArray.to_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.to_tuples.html#pandas.arrays.IntervalArray.to_tuples "pandas.arrays.IntervalArray.to_tuples")

Analogous method for IntervalArray.

Examples

\>>> idx \= pd.interval\_range(start\=0, end\=2)
\>>> idx
IntervalIndex(\[(0, 1\], (1, 2\]\], dtype='interval\[int64, right\]')
\>>> idx.to\_tuples()
Index(\[(0, 1), (1, 2)\], dtype='object')

Copy to clipboard

On this page