[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.names.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.names.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.names.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.names.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.names.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.names.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.names.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.names.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.names.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.names.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.names.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.names.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.names.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.names.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.names[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.names.html#pandas-index-names "Link to this heading")

======================================================================================================================================

property Index.names[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L1949-L1982)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.names.html#pandas.Index.names "Link to this definition")

Get names on index.

This method returns a FrozenList containing the names of the object. It’s primarily intended for internal use.

Returns:

FrozenList

A FrozenList containing the object’s names, contains None if the object does not have a name.

See also

[`Index.name`](https://pandas.pydata.org/docs/reference/api/pandas.Index.name.html#pandas.Index.name "pandas.Index.name")

Index name as a string, or None for MultiIndex.

Examples

\>>> idx \= pd.Index(\[1, 2, 3\], name\="x")
\>>> idx.names
FrozenList(\['x'\])

Copy to clipboard

\>>> idx \= pd.Index(\[1, 2, 3\], name\=("x", "y"))
\>>> idx.names
FrozenList(\[('x', 'y')\])

Copy to clipboard

If the index does not have a name set:

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx.names
FrozenList(\[None\])

Copy to clipboard

On this page