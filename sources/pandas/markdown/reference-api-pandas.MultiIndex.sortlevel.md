[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.sortlevel.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.sortlevel.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.sortlevel.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.sortlevel.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.sortlevel.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.sortlevel.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.sortlevel.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.sortlevel.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.sortlevel.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.sortlevel.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.sortlevel.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.sortlevel.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.sortlevel.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.sortlevel.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.sortlevel[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.sortlevel.html#pandas-multiindex-sortlevel "Link to this heading")

=================================================================================================================================================================

MultiIndex.sortlevel(_level\=0_, _ascending\=True_, _sort\_remaining\=True_, _na\_position\='first'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L3214-L3346)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.sortlevel.html#pandas.MultiIndex.sortlevel "Link to this definition")

Sort MultiIndex at the requested level.

This method is useful when dealing with MultiIndex objects, allowing for sorting at a specific level of the index. The function preserves the relative ordering of data within the same level while sorting the overall MultiIndex. The method provides flexibility with the ascending parameter to define the sort order and with the sort\_remaining parameter to control whether the remaining levels should also be sorted. Sorting a MultiIndex can be crucial when performing operations that require ordered indices, such as grouping or merging datasets. The na\_position argument is important in handling missing values consistently across different levels.

Parameters:

**level**list-like, int or str, default 0

If a string is given, must be a name of the level. If list-like must be names or ints of levels.

**ascending**bool, default True

False to sort in descending order. Can also be a list to specify a directed ordering.

**sort\_remaining**bool, default True

If True, sorts by the remaining levels after sorting by the specified level.

**na\_position**{‘first’ or ‘last’}, default ‘first’

Argument ‘first’ puts NaNs at the beginning, ‘last’ puts NaNs at the end.

Added in version 2.1.0.

Returns:

**sorted\_index**pd.MultiIndex

Resulting index.

**indexer**np.ndarray\[np.intp\]

Indices of output values in original index.

See also

[`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")

A multi-level, or hierarchical, index object for pandas objects.

[`Index.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.sort_values.html#pandas.Index.sort_values "pandas.Index.sort_values")

Sort Index values.

[`DataFrame.sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index")

Sort DataFrame by the index.

[`Series.sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html#pandas.Series.sort_index "pandas.Series.sort_index")

Sort Series by the index.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[\[0, 0\], \[2, 1\]\])
\>>> mi
MultiIndex(\[(0, 2),\
            (0, 1)\],
           )

Copy to clipboard

\>>> mi.sortlevel()
(MultiIndex(\[(0, 1),\
            (0, 2)\],
           ), array(\[1, 0\]))

Copy to clipboard

\>>> mi.sortlevel(sort\_remaining\=False)
(MultiIndex(\[(0, 2),\
            (0, 1)\],
           ), array(\[0, 1\]))

Copy to clipboard

\>>> mi.sortlevel(1)
(MultiIndex(\[(0, 1),\
            (0, 2)\],
           ), array(\[1, 0\]))

Copy to clipboard

\>>> mi.sortlevel(1, ascending\=False)
(MultiIndex(\[(0, 2),\
            (0, 1)\],
           ), array(\[0, 1\]))

Copy to clipboard

On this page