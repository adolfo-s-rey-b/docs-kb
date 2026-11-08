[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.sort_values.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.sort_values.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.sort_values.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.sort_values.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.sort_values.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.sort_values.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.sort_values.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.sort_values.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.sort_values.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.sort_values.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.sort_values.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.sort_values.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.sort_values.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.sort_values.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.sort\_values[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.sort_values.html#pandas-index-sort-values "Link to this heading")

=========================================================================================================================================================

Index.sort\_values(_\*_, _return\_indexer\=False_, _ascending\=True_, _na\_position\='last'_, _key\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L6176-L6262)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.sort_values.html#pandas.Index.sort_values "Link to this definition")

Return a sorted copy of the index.

Return a sorted copy of the index, and optionally return the indices that sorted the index itself.

Parameters:

**return\_indexer**bool, default False

Should the indices that would sort the index be returned.

**ascending**bool, default True

Should the index values be sorted in an ascending order.

**na\_position**{‘first’ or ‘last’}, default ‘last’

Argument ‘first’ puts NaNs at the beginning, ‘last’ puts NaNs at the end.

**key**callable, optional

If not None, apply the key function to the index values before sorting. This is similar to the key argument in the builtin `sorted()` function, with the notable difference that this key function should be _vectorized_. It should expect an `Index` and return an `Index` of the same shape.

Returns:

**sorted\_index**pandas.Index

Sorted copy of the index.

**indexer**numpy.ndarray, optional

The indices that the index itself was sorted by.

See also

[`Series.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values "pandas.Series.sort_values")

Sort values of a Series.

[`DataFrame.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")

Sort values in a DataFrame.

Examples

\>>> idx \= pd.Index(\[10, 100, 1, 1000\])
\>>> idx
Index(\[10, 100, 1, 1000\], dtype='int64')

Copy to clipboard

Sort values in ascending order (default behavior).

\>>> idx.sort\_values()
Index(\[1, 10, 100, 1000\], dtype='int64')

Copy to clipboard

Sort values in descending order, and also get the indices idx was sorted by.

\>>> idx.sort\_values(ascending\=False, return\_indexer\=True)
(Index(\[1000, 100, 10, 1\], dtype='int64'), array(\[3, 1, 0, 2\]))

Copy to clipboard

On this page