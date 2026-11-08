[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.from\_arrays[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas-multiindex-from-arrays "Link to this heading")

========================================================================================================================================================================

classmethod MultiIndex.from\_arrays(_arrays_, _sortorder\=None_, _names\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L466-L539)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "Link to this definition")

Convert arrays to MultiIndex.

Each array in the input corresponds to one level of the output MultiIndex. The i-th element of each array together form the i-th tuple in the resulting MultiIndex.

Parameters:

**arrays**list / sequence of array-likes

Each array-like gives one level’s value for each data point. len(arrays) is the number of levels.

**sortorder**int or None

Level of sortedness (must be lexicographically sorted by that level).

**names**list / sequence of str, optional

Names for the levels in the index.

Returns:

MultiIndex

See also

[`MultiIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")

Convert list of tuples to MultiIndex.

[`MultiIndex.from_product`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas.MultiIndex.from_product "pandas.MultiIndex.from_product")

Make a MultiIndex from cartesian product of iterables.

[`MultiIndex.from_frame`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame "pandas.MultiIndex.from_frame")

Make a MultiIndex from a DataFrame.

Examples

\>>> arrays \= \[\[1, 1, 2, 2\], \["red", "blue", "red", "blue"\]\]
\>>> pd.MultiIndex.from\_arrays(arrays, names\=("number", "color"))
MultiIndex(\[(1,  'red'),\
            (1, 'blue'),\
            (2,  'red'),\
            (2, 'blue')\],
           names=\['number', 'color'\])

Copy to clipboard

On this page