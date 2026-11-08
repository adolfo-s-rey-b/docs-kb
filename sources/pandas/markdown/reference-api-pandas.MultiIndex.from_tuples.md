[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.from_tuples.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.from_tuples.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.from_tuples.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.from_tuples.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.from_tuples.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.from_tuples.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.from_tuples.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.from_tuples.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.from_tuples.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.from_tuples.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.from_tuples.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.from_tuples.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.from\_tuples[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas-multiindex-from-tuples "Link to this heading")

========================================================================================================================================================================

classmethod MultiIndex.from\_tuples(_tuples_, _sortorder\=None_, _names\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L541-L623)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "Link to this definition")

Convert list of tuples to MultiIndex.

Each tuple in the input represents a single entry in the resulting MultiIndex. The number of elements in each tuple determines the number of levels.

Parameters:

**tuples**list-like of tuples

Each tuple is the index of one row/column.

**sortorder**int or None

Level of sortedness (must be lexicographically sorted by that level).

**names**list / sequence of str, optional

Names for the levels in the index.

Returns:

MultiIndex

See also

[`MultiIndex.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")

Convert list of arrays to MultiIndex.

[`MultiIndex.from_product`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas.MultiIndex.from_product "pandas.MultiIndex.from_product")

Make a MultiIndex from cartesian product of iterables.

[`MultiIndex.from_frame`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame "pandas.MultiIndex.from_frame")

Make a MultiIndex from a DataFrame.

Examples

\>>> tuples \= \[(1, "red"), (1, "blue"), (2, "red"), (2, "blue")\]
\>>> pd.MultiIndex.from\_tuples(tuples, names\=("number", "color"))
MultiIndex(\[(1,  'red'),\
            (1, 'blue'),\
            (2,  'red'),\
            (2, 'blue')\],
           names=\['number', 'color'\])

Copy to clipboard

On this page