[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.append.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.append.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.append.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.append.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.append.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.append.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.append.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.append.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.append.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.append.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.append.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.append.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.append.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.append.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.append[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.append.html#pandas-multiindex-append "Link to this heading")

========================================================================================================================================================

MultiIndex.append(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L2710-L2784)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.append.html#pandas.MultiIndex.append "Link to this definition")

Append a collection of Index options together.

The append method is used to combine multiple Index objects into a single Index. This is particularly useful when dealing with multi-level indexing (MultiIndex) where you might need to concatenate different levels of indices. The method handles the alignment of the levels and codes of the indices being appended to ensure consistency in the resulting MultiIndex.

Parameters:

**other**Index or list/tuple of indices

Index or list/tuple of Index objects to be appended.

Returns:

Index

The combined index.

See also

[`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")

A multi-level, or hierarchical, index object for pandas objects.

[`Index.append`](https://pandas.pydata.org/docs/reference/api/pandas.Index.append.html#pandas.Index.append "pandas.Index.append")

Append a collection of Index options together.

[`concat`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat "pandas.concat")

Concatenate pandas objects along a particular axis.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[\["a"\], \["b"\]\])
\>>> mi
MultiIndex(\[('a', 'b')\],
           )
\>>> mi.append(mi)
MultiIndex(\[('a', 'b'), ('a', 'b')\],
           )

Copy to clipboard

On this page