[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.from\_frame[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas-multiindex-from-frame "Link to this heading")

=====================================================================================================================================================================

classmethod MultiIndex.from\_frame(_df_, _sortorder\=None_, _names\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L690-L761)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame "Link to this definition")

Make a MultiIndex from a DataFrame.

Each column of the DataFrame becomes one level of the MultiIndex, with the column values used as labels.

Parameters:

**df**DataFrame

DataFrame to be converted to MultiIndex.

**sortorder**int, optional

Level of sortedness (must be lexicographically sorted by that level).

**names**list-like, optional

If no names are provided, use the column names, or tuple of column names if the columns is a MultiIndex. If a sequence, overwrite names with the given sequence.

Returns:

MultiIndex

The MultiIndex representation of the given DataFrame.

See also

[`MultiIndex.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")

Convert list of arrays to MultiIndex.

[`MultiIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")

Convert list of tuples to MultiIndex.

[`MultiIndex.from_product`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas.MultiIndex.from_product "pandas.MultiIndex.from_product")

Make a MultiIndex from cartesian product of iterables.

Examples

\>>> df \= pd.DataFrame(
...     \[\["HI", "Temp"\], \["HI", "Precip"\], \["NJ", "Temp"\], \["NJ", "Precip"\]\],
...     columns\=\["a", "b"\],
... )
\>>> df
      a       b
0    HI    Temp
1    HI  Precip
2    NJ    Temp
3    NJ  Precip

Copy to clipboard

\>>> pd.MultiIndex.from\_frame(df)
MultiIndex(\[('HI',   'Temp'),\
            ('HI', 'Precip'),\
            ('NJ',   'Temp'),\
            ('NJ', 'Precip')\],
           names=\['a', 'b'\])

Copy to clipboard

Using explicit names, instead of the column names

\>>> pd.MultiIndex.from\_frame(df, names\=\["state", "observation"\])
MultiIndex(\[('HI',   'Temp'),\
            ('HI', 'Precip'),\
            ('NJ',   'Temp'),\
            ('NJ', 'Precip')\],
           names=\['state', 'observation'\])

Copy to clipboard

On this page