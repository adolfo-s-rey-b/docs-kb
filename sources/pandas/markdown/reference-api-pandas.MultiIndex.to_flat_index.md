[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_flat_index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.to_flat_index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_flat_index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.to_flat_index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.to_flat_index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.to_flat_index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.to_flat_index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.to_flat_index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.to_flat_index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.to_flat_index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.to_flat_index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.to_flat_index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.to_flat_index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.to_flat_index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.to\_flat\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_flat_index.html#pandas-multiindex-to-flat-index "Link to this heading")

===============================================================================================================================================================================

MultiIndex.to\_flat\_index()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L2280-L2311)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_flat_index.html#pandas.MultiIndex.to_flat_index "Link to this definition")

Convert a MultiIndex to an Index of Tuples containing the level values.

This is useful for compatibility with libraries or operations that expect a flat, single-level index rather than a hierarchical one.

Returns:

pd.Index

Index with the MultiIndex data represented in Tuples.

See also

[`MultiIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")

Convert flat index back to MultiIndex.

Notes

This method will simply return the caller if called by anything other than a MultiIndex.

Examples

\>>> index \= pd.MultiIndex.from\_product(
...     \[\["foo", "bar"\], \["baz", "qux"\]\], names\=\["a", "b"\]
... )
\>>> index.to\_flat\_index()
Index(\[('foo', 'baz'), ('foo', 'qux'),\
       ('bar', 'baz'), ('bar', 'qux')\],
      dtype='object')

Copy to clipboard

On this page