[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.get_loc.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalIndex.get_loc.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.get_loc.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalIndex.get_loc.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalIndex.get_loc.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalIndex.get_loc.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalIndex.get_loc.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalIndex.get_loc.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalIndex.get_loc.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalIndex.get_loc.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalIndex.get_loc.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalIndex.get_loc.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalIndex.get_loc.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalIndex.get_loc.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalIndex.get\_loc[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.get_loc.html#pandas-intervalindex-get-loc "Link to this heading")

=====================================================================================================================================================================

IntervalIndex.get\_loc(_key_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/interval.py#L1099-L1178)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.get_loc.html#pandas.IntervalIndex.get_loc "Link to this definition")

Get integer location, slice or boolean mask for requested label.

The get\_loc method is used to retrieve the integer index, a slice for slicing objects, or a boolean mask indicating the presence of the label in the IntervalIndex.

Parameters:

**key**label

The value or range to find in the IntervalIndex.

Returns:

int if unique index, slice if monotonic index, else mask

The position or positions found. This could be a single number, a range, or an array of true/false values indicating the position(s) of the label.

See also

`IntervalIndex.get_indexer_non_unique`

Compute indexer and mask for new index given the current index.

[`Index.get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html#pandas.Index.get_loc "pandas.Index.get_loc")

Similar method in the base Index class.

Examples

\>>> i1, i2 \= pd.Interval(0, 1), pd.Interval(1, 2)
\>>> index \= pd.IntervalIndex(\[i1, i2\])
\>>> index.get\_loc(1)
0

Copy to clipboard

You can also supply a point inside an interval.

\>>> index.get\_loc(1.5)
1

Copy to clipboard

If a label is in several intervals, you get the locations of all the relevant intervals.

\>>> i3 \= pd.Interval(0, 2)
\>>> overlapping\_index \= pd.IntervalIndex(\[i1, i2, i3\])
\>>> overlapping\_index.get\_loc(0.5)
array(\[ True, False,  True\])

Copy to clipboard

Only exact matches will be returned if an interval is provided.

\>>> index.get\_loc(pd.Interval(0, 1))
0

Copy to clipboard

On this page