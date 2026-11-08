[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.from\_product[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas-multiindex-from-product "Link to this heading")

===========================================================================================================================================================================

classmethod MultiIndex.from\_product(_iterables_, _sortorder\=None_, _names\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L625-L688)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas.MultiIndex.from_product "Link to this definition")

Make a MultiIndex from the cartesian product of multiple iterables.

This method generates a MultiIndex containing all combinations of the input iterables, similar to computing the cartesian product.

Parameters:

**iterables**list / sequence of iterables

Each iterable gives the labels for one level of the index. Labels that compare equal (e.g. `1`, `1.0` and `True`) are collapsed into a single label; the first occurrence determines the value stored in the level.

**sortorder**int or None

Level of sortedness (must be lexicographically sorted by that level).

**names**list / sequence of str, optional

Names for the levels in the index. If not explicitly provided, names will be inferred from the elements of iterables if an element has a name attribute.

Returns:

MultiIndex

See also

[`MultiIndex.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")

Convert list of arrays to MultiIndex.

[`MultiIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")

Convert list of tuples to MultiIndex.

[`MultiIndex.from_frame`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame "pandas.MultiIndex.from_frame")

Make a MultiIndex from a DataFrame.

Examples

\>>> numbers \= \[0, 1, 2\]
\>>> colors \= \["green", "purple"\]
\>>> pd.MultiIndex.from\_product(\[numbers, colors\], names\=\["number", "color"\])
MultiIndex(\[(0,  'green'),\
            (0, 'purple'),\
            (1,  'green'),\
            (1, 'purple'),\
            (2,  'green'),\
            (2, 'purple')\],
           names=\['number', 'color'\])

Copy to clipboard

On this page